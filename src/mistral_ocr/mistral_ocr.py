from pathlib import Path
import os
import json

from mistralai import Mistral
from mistralai import DocumentURLChunk, ImageURLChunk, TextChunk
from mistralai.models import OCRResponse

from ._ocrutils import (
    replace_images_in_markdown,
    save_base64_to_image,
)

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])


class MyMistralOCRpdf:
    """
    A class for performing OCR on PDF files using Mistral's OCR API.
    
    This class provides functionality to extract text from PDF documents
    and convert the OCR results to markdown format, with options to include
    inline images and save extracted images to disk.
    
    Parameters
    ----------
    file_path : str or Path
        Path to the PDF file to be processed
    image_folder_path : str or Path
        Directory path where extracted images will be saved
        
    Attributes
    ----------
    file_path : Path
        Path to the PDF file being processed
    image_folder_path : Path  
        Directory path where extracted images will be saved
    ocr_response : OCRResponse or None
        Response object from Mistral OCR API containing the OCR results,
        initially None until `ocr_pdf()` is called
        
    Raises
    ------
    FileNotFoundError
        If the specified PDF file does not exist
    NotADirectoryError
        If the specified image folder path does not exist
    """

    def __init__(self, 
                 file_path: str | Path,
                 image_folder_path: str | Path):
        self.file_path = Path(file_path)
        self.image_folder_path = Path(image_folder_path)
        self.ocr_response = None
        
        if not self.file_path.is_file():
            raise FileNotFoundError(f"The file '{self.file_path}' does not exist.")
        
        if not self.image_folder_path.is_dir():
            raise NotADirectoryError(f"The directory '{self.image_folder_path}' does not exist.")
            
        
    def __repr__(self):
        ocr_status = "processed" if self.ocr_response else "not processed"
        return f"MyMistralOCR(file_path='{self.file_path}', image_folder_path='{self.image_folder_path}', ocr_status='{ocr_status}', ocr_response={self.ocr_response})"

    def ocr_pdf(self):
        """OCR one PDF file"""

        uploaded_file = client.files.upload(
            file={
                "file_name": self.file_path.stem,
                "content": self.file_path.read_bytes(),
            },
            purpose="ocr",
        )

        signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)

        self.ocr_response = client.ocr.process(
            document=DocumentURLChunk(document_url=signed_url.url),
            model="mistral-ocr-latest",
            include_image_base64=True,
        )

        return self.ocr_response

    def to_markdown(self):
        return "\n\n".join([page.markdown for page in self.ocr_response.pages])

    def to_markdown_with_inline_img(self):
        markdowns: list[str] = []
        for page in self.ocr_response.pages:
            image_data = {}
            for img in page.images:
                image_data[img.id] = img.image_base64
            markdowns.append(
                replace_images_in_markdown(page.markdown, image_data)
            )
        return "\n\n".join(markdowns)
    
    def save_images(self):
        """
        Save all images extracted from the OCR process to the specified folder.
        
        Extracts all images from the OCR results and saves them to the 
        image folder path specified during initialization.
        """
        if self.ocr_response is None:
            raise AttributeError("OCR has not been run yet. Call ocr_pdf() first.")
            
        results = {}
        for page in self.ocr_response.pages:
            for img in page.images:
                output_path = Path(self.image_folder_path, f"{img.id}")
                success = save_base64_to_image(img.image_base64, output_path)
                results[img.id] = success
        
        return results

class MyMistralOCRpdfMulti:
    """
    A class for performing OCR on multiple PDF files in a directory.
    
    This class processes all PDF files in an input directory and outputs
    the OCR results as markdown files in the specified output directory.
    
    Parameters
    ----------
    dir_input : str
        Path to the directory containing PDF files to process
    dir_output : str
        Path to the directory where markdown output files will be saved
    dir_image : str, optional
        Path to the parent directory where extracted images will be saved.
        For each PDF, a subfolder with snake_case version of the PDF filename 
        will be created under this directory
    inline_image : bool, optional
        Whether to include base64-encoded images inline in the markdown, by default False
    filename_suffix : str, optional
        Suffix to add to the end of each file name when write to disk, by default ""
    filename_prefix : str, optional
        Prefix to add to the beginning of each file name when write to disk, by default ""
    
    Attributes
    ----------
    dir_input : Path
        Input directory path
    dir_output : Path
        Output directory path
    dir_image : Path or None
        Parent directory path for image storage
    inline_image : bool
        Flag to determine if images should be included inline
    filename_suffix : str
        Suffix to add to each output filename
    filename_prefix : str
        Prefix to add to each output filename
    processed_files : list
        List of successfully processed files
    failed_files : dict
        Dictionary of files that failed processing and their error messages
    """

    def __init__(self, dir_input: str, dir_output: str, dir_image: str = None,
                 inline_image: bool = False, filename_suffix: str = "", 
                 filename_prefix: str = ""):
        self.dir_input = Path(dir_input)
        self.dir_output = Path(dir_output)
        self.dir_image = Path(dir_image) if dir_image else None
        self.inline_image = inline_image
        self.filename_suffix = filename_suffix
        self.filename_prefix = filename_prefix
        self.processed_files = []
        self.failed_files = {}
        
        # Create output directory if it doesn't exist
        self.dir_output.mkdir(parents=True, exist_ok=True)
        
        # Create image parent directory if provided
        if self.dir_image:
            self.dir_image.mkdir(parents=True, exist_ok=True)
        
        if not self.dir_input.is_dir():
            raise NotADirectoryError(f"Input directory '{self.dir_input}' does not exist.")

    def _to_snake_case(self, text: str) -> str:
        """
        Convert text to snake_case format.
        
        Parameters
        ----------
        text : str
            Text to convert to snake_case
            
        Returns
        -------
        str
            Text in snake_case format
        """
        # Replace spaces and special characters with underscores
        import re
        text = text.lower()
        # Replace spaces and non-alphanumeric chars (except underscores) with underscores
        text = re.sub(r'[^\w]|[\s]', '_', text)
        # Replace multiple consecutive underscores with a single one
        text = re.sub(r'_+', '_', text)
        # Remove leading/trailing underscores
        return text.strip('_')

    def execute(self):
        """
        Process all PDF files in the input directory.
        
        Iterates through all PDF files in the input directory, performs OCR on each,
        and saves the results as markdown files in the output directory. If `dir_image` 
        is specified, extracts and saves images from each PDF to its own subfolder.
        
        Returns
        -------
        dict
            A summary of the processing results containing:
            - 'processed': list of successfully processed files
            - 'failed': dict of failed files and their error messages
            - 'total': total number of PDF files found
        """
        pdf_files = list(self.dir_input.glob("*.pdf"))
        
        for pdf_file in pdf_files:
            output_filename = f"{self.filename_prefix}{pdf_file.stem}{self.filename_suffix}.md"
            output_file = self.dir_output / output_filename
            
            try:
                # Create image folder if dir_image is specified
                image_folder = None
                if self.dir_image:
                    snake_name = self._to_snake_case(pdf_file.stem)
                    image_folder = self.dir_image / snake_name
                    image_folder.mkdir(exist_ok=True)
                    ocr = MyMistralOCRpdf(pdf_file, image_folder)
                else:
                    # If dir_image not provided, don't attempt to save images
                    ocr = MyMistralOCRpdf(pdf_file, Path("."))  # Use current directory as placeholder
                
                ocr.ocr_pdf()
                
                # Choose markdown format based on inline_image flag
                if self.inline_image:
                    markdown_content = ocr.to_markdown_with_inline_img()
                else:
                    markdown_content = ocr.to_markdown()
                
                # Write markdown to output file
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                
                # If image folder is provided, save extracted images
                if image_folder:
                    ocr.save_images()
                
                self.processed_files.append(str(pdf_file))
                
            except Exception as e:
                self.failed_files[str(pdf_file)] = str(e)
        
        return {
            "processed": self.processed_files,
            "failed": self.failed_files,
            "total": len(pdf_files)
        }
    
    def __repr__(self):
        return f"MyMistralOCRpdfMulti(dir_input='{self.dir_input}', dir_output='{self.dir_output}', dir_image='{self.dir_image}', inline_image={self.inline_image}, filename_suffix='{self.filename_suffix}', filename_prefix='{self.filename_prefix}')"