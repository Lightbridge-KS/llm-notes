from pathlib import Path
import os
import json

from mistralai import Mistral
from mistralai import DocumentURLChunk, ImageURLChunk, TextChunk
from mistralai.models import OCRResponse


client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])


class MyMistralOCRpdf:
    """
    A class for performing OCR on PDF files using Mistral's OCR API.
    This class provides functionality to extract text from PDF documents
    and convert the OCR results to markdown format, with options to include
    inline images.
    Attributes:
        file_path (Path): Path to the PDF file to be processed
        ocr_response: The response object from Mistral OCR API containing
                      the OCR results
    Methods:
        ocr_pdf(): Process the PDF file with Mistral OCR
        to_markdown(): Convert OCR results to markdown text
        to_markdown_with_inline_img(): Convert OCR results to markdown with embedded base64 images
        _replace_images_in_markdown(): Helper method to replace image references with base64 data
    """

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)
        self.ocr_response = None

    def __repr__(self):
        ocr_status = "processed" if self.ocr_response else "not processed"
        return f"MyMistralOCR(file_path='{self.file_path}', ocr_status='{ocr_status}')"

    def ocr_pdf(self):
        """OCR one PDF file"""

        pdf_file = self.file_path
        if not pdf_file.is_file():
            raise FileNotFoundError(f"The file '{pdf_file}' does not exist.")

        uploaded_file = client.files.upload(
            file={
                "file_name": pdf_file.stem,
                "content": pdf_file.read_bytes(),
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
                self._replace_images_in_markdown(page.markdown, image_data)
            )
        return "\n\n".join(markdowns)

    @staticmethod
    def _replace_images_in_markdown(markdown_str: str, images_dict: dict) -> str:
        for img_name, base64_str in images_dict.items():
            markdown_str = markdown_str.replace(
                f"![{img_name}]({img_name})", f"![{img_name}]({base64_str})"
            )
        return markdown_str



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

    def __init__(self, dir_input: str, dir_output: str, inline_image: bool = False, 
                 filename_suffix: str = "", filename_prefix: str = ""):
        self.dir_input = Path(dir_input)
        self.dir_output = Path(dir_output)
        self.inline_image = inline_image
        self.filename_suffix = filename_suffix
        self.filename_prefix = filename_prefix
        self.processed_files = []
        self.failed_files = {}
        
        # Create output directory if it doesn't exist
        self.dir_output.mkdir(parents=True, exist_ok=True)
        
        if not self.dir_input.is_dir():
            raise NotADirectoryError(f"Input directory '{self.dir_input}' does not exist.")

    def execute(self):
        """
        Process all PDF files in the input directory.
        
        Iterates through all PDF files in the input directory, performs OCR on each,
        and saves the results as markdown files in the output directory.
        
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
                ocr = MyMistralOCRpdf(pdf_file)
                ocr.ocr_pdf()
                
                # Choose markdown format based on inline_image flag
                if self.inline_image:
                    markdown_content = ocr.to_markdown_with_inline_img()
                else:
                    markdown_content = ocr.to_markdown()
                
                # Write markdown to output file
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                
                self.processed_files.append(str(pdf_file))
                
            except Exception as e:
                self.failed_files[str(pdf_file)] = str(e)
        
        return {
            "processed": self.processed_files,
            "failed": self.failed_files,
            "total": len(pdf_files)
        }
    
    def __repr__(self):
        return f"MyMistralOCRpdfMulti(dir_input='{self.dir_input}', dir_output='{self.dir_output}', inline_image={self.inline_image}, filename_suffix='{self.filename_suffix}', filename_prefix='{self.filename_prefix}')"