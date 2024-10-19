import os
from openai import OpenAI

from ..pdftools.pdf2image import pdf_to_base64_images

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def ocr_pdf_to_markdown(pdf_path: str, **kwarg):
    """OCR PDF to Markdown text."""
    base64_images = pdf_to_base64_images(pdf_path)
    try:
        md_text = ocr_image_to_markdown(base64_images, **kwarg)
        return md_text
    except Exception as e:
        print(f"Error extract PDF: {e}")
        return []

def ocr_image_to_markdown(base64_images: list[str] | str, **kwarg):
    """Convert one or multiple base64-encoded images to Markdown text."""
    # Single Image
    is_single_image = all([len(x) == 1 for x in base64_images])
    if is_single_image:
        md_text = ocr_single_image_to_markdown(base64_images, **kwarg)
        return md_text
    # Multiple Images
    try:
        
        md_text_ls = [ocr_single_image_to_markdown(base64_image, **kwarg) for base64_image in base64_images] 
        md_text_ls_rm_blank = list(filter(None, md_text_ls)) # Remove blank string ("")
        md_text = "\n\n---\n\n".join(md_text_ls_rm_blank)
        return md_text
    
    except Exception as e:
        print(f"Error extract Image: {e}")
        return []
    
    
def ocr_single_image_to_markdown(base64_image, 
                                 model = "gpt-4o",
                                 md_format = "Github-flavored markdown",
                                 heading_lv_max = "H2"
                                 ):
    system_prompt = f"""
    You are an advanced OCR-based data extraction tool designed to convert text, tables, and structured content from images into {md_format}. Ensure the output retains the original layout and information integrity as closely as possible. Include headers, bullet points, or tables where appropriate, and optimize for readability in Markdown syntax.
    
    **Heading level:** The highest level of heading is {heading_lv_max}. 
    **LaTeX Math expression**
    - Inline: surround the inline expression with dollar symbols, for example: $\pi$
    - Blocks: delimit the block expression with two dollar symbols, for example:
      $$
      E = m \times c^2 
      $$
    
    Return markdown text output without enclosing in code block. If the image is blank or no appropriate content can be extracted, return empty text string ("").  
    """
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Convert data from this image to markdown text"},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}", "detail": "high"}}
                ]
            }
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content
