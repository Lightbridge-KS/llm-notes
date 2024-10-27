import os
from openai import OpenAI

from ..pdftools.pdf2image import pdf_to_base64_images

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


from .mem_vision import get_completions_vision_mem_df


def ocr_pdf_batch_to_markdown(pdf_path: str, batch_size = 3, **kwarg):
    """OCR PDF to Markdown text with Memory Batched."""
    base64_images = pdf_to_base64_images(pdf_path)
    try:
        md_text = ocr_image_batch_to_markdown(base64_images, batch_size = batch_size, **kwarg)
        return md_text
    except Exception as e:
        print(f"Error extract PDF: {e}")
        return []

def ocr_image_batch_to_markdown(base64_images: list[str] | str, batch_size = 3, **kwarg):
    """Convert one or multiple base64-encoded images to Markdown text with batched memory."""
    
    # Single Page
    is_single_image = all([len(x) == 1 for x in base64_images])
    if is_single_image:
        md_text = ocr_batch_image_to_markdown(base64_images, **kwarg)
        return md_text
    
    # Multiple Pages
    base64_images_batched = _slice_list(base64_images, batch_size = batch_size)
    
    out_ls_nested = [] # Will be Nested list
    
    for base64_images_ls in base64_images_batched:
        md_text_ls = ocr_batch_image_to_markdown(base64_images_ls, **kwarg)
        md_text_ls_rm_blank = list(filter(None, md_text_ls)) # Remove blank string ("")
        out_ls_nested.append(md_text_ls_rm_blank) 
        
    out_ls = [item for sublist in out_ls_nested for item in sublist] # Un-nest List
    md_text = "\n\n---\n\n".join(out_ls)
        
    return md_text
    

def ocr_batch_image_to_markdown(base64_images, 
                                model = "gpt-4o",
                                md_format = "Github-flavored markdown",
                                heading_lv_max = "H2"
                                ):
    system_prompt = f"""
    You are an advanced OCR-based data extraction tool designed to convert text, tables, and structured content from images of document pages into {md_format}. 
    - Each image will represent a single page of a document.
    - Ensure the output retains the original layout and information integrity as closely as possible. Include headers, bullet points, or tables where appropriate, and optimize for readability in Markdown syntax.
    
    Here are the Markdown specification:
    **Heading level:** The highest level of heading is {heading_lv_max}. 
    **LaTeX Math expression**
    - Inline: surround the inline expression with dollar symbols, for example: $1+1 = 2$
    - Blocks: delimit the block expression with two dollar symbols, for example:
      $$
      E = m \times c^2 
      $$
    
    Return markdown text output without enclosing in code block. If any page is blank or no appropriate content can be extracted, return empty text string ("").  
    """
    
    response_df = get_completions_vision_mem_df(image_prompt="Convert data from this page to markdown text",
                                                image_prompt_next="Next page",
                                                base64_images=base64_images,
                                                system_prompt=system_prompt,
                                                model=model)
    
    response_ls = response_df["assistant_text"].to_list()
    
    return response_ls



def _slice_list(ls, batch_size):
    """Split a list into sublists with a maximum length of `batch_size`."""
    return [ls[i:(i + batch_size)] for i in range(0, len(ls), batch_size)]