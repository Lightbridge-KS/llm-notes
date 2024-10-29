import os
from typing import List, Optional
from openai import OpenAI

from ..pdftools.pdf2image import pdf_to_base64_images
from .mem_vision import get_completions_vision_mem_df

class PDFMarkdownConverter:
    """A class for converting PDF documents to Markdown format with batch processing capabilities.
    
    This class provides functionality to convert PDF documents to Markdown format using OpenAI's
    vision model. It supports both single and multi-page documents with batched processing for
    better memory management.
    
    Parameters
    ----------
    api_key : str, optional
        OpenAI API key. If not provided, will attempt to get from environment variable
    model : str, optional
        OpenAI model to use for conversion, by default "gpt-4o"
    md_format : str, optional
        Markdown format specification, by default "Github-flavored markdown"
    heading_lv_max : str, optional
        Maximum heading level to use, by default "H2"
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4o",
        md_format: str = "Github-flavored markdown",
        heading_lv_max: str = "H2"
    ):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.md_format = md_format
        self.heading_lv_max = heading_lv_max
        self._system_prompt = self._create_system_prompt()

    def _create_system_prompt(self) -> str:
        """Create the system prompt for the OpenAI model.
        
        Returns
        -------
        str
            Formatted system prompt
        """
        return f"""
        You are an advanced OCR-based data extraction tool designed to convert text, tables, and structured content from images of document pages into {self.md_format}. 
        - Each image will represent a single page of a document.
        - Ensure the output retains the original layout and information integrity as closely as possible. Include headers, bullet points, or tables where appropriate, and optimize for readability in Markdown syntax.
        
        Here are the Markdown specification:
        **Heading level:** The highest level of heading is {self.heading_lv_max}. 
        **LaTeX Math expression**
        - Inline: surround the inline expression with dollar symbols, for example: $1+1 = 2$
        - Blocks: delimit the block expression with two dollar symbols, for example:
          $$
          E = m \times c^2 
          $$
        
        Return markdown text output without enclosing in code block. If any page is blank or no appropriate content can be extracted, return empty text string ("").  
        """

    @staticmethod
    def _slice_list(ls: list, batch_size: int) -> List[list]:
        """Split a list into sublists with a maximum length of batch_size.
        
        Parameters
        ----------
        ls : list
            Input list to be sliced
        batch_size : int
            Maximum size of each batch
            
        Returns
        -------
        List[list]
            List of sublists, each with maximum length of batch_size
        """
        return [ls[i:(i + batch_size)] for i in range(0, len(ls), batch_size)]

    def convert_pdf(self, pdf_path: str, batch_size: int = 3) -> str:
        """Convert a PDF file to Markdown text with memory-efficient batch processing.
        
        Parameters
        ----------
        pdf_path : str
            Path to the PDF file
        batch_size : int, optional
            Number of pages to process in each batch, by default 3
            
        Returns
        -------
        str
            Converted markdown text
            
        Raises
        ------
        Exception
            If PDF conversion fails
        """
        try:
            base64_images = pdf_to_base64_images(pdf_path)
            return self.convert_images(base64_images, batch_size=batch_size)
        except Exception as e:
            raise Exception(f"Error converting PDF: {e}")

    def convert_images(self, base64_images: List[str] | str, batch_size: int = 3) -> str:
        """Convert one or multiple base64-encoded images to Markdown text with batched memory.
        
        Parameters
        ----------
        base64_images : List[str] | str
            List of base64-encoded images or single base64 string
        batch_size : int, optional
            Number of images to process in each batch, by default 3
            
        Returns
        -------
        str
            Converted markdown text
        """
        # Handle single page
        is_single_image = all([len(x) == 1 for x in base64_images])
        if is_single_image:
            return self._process_batch(base64_images)
        
        # Handle multiple pages with batching
        base64_images_batched = self._slice_list(base64_images, batch_size)
        markdown_sections = []
        
        for image_batch in base64_images_batched:
            batch_text = self._process_batch(image_batch)
            if batch_text:  # Only add non-empty sections
                markdown_sections.extend(batch_text)
        
        return "\n\n---\n\n".join(markdown_sections)

    def _process_batch(self, base64_images: List[str]) -> List[str]:
        """Process a batch of images and convert them to markdown.
        
        Parameters
        ----------
        base64_images : List[str]
            List of base64-encoded images to process
            
        Returns
        -------
        List[str]
            List of markdown text sections
        """
        response_df = get_completions_vision_mem_df(
            image_prompt="Convert data from this page to markdown text",
            image_prompt_next="Next page",
            base64_images=base64_images,
            system_prompt=self._system_prompt,
            model=self.model
        )
        
        responses = response_df["assistant_text"].to_list()
        return [r for r in responses if r]  # Filter out empty responses
