import os
import io
import base64

import pymupdf
from PIL import Image


def pdf_to_base64_images(pdf_path):
    """Convert each page of a PDF to a Base64-encoded PNG image."""
    try:
        # Open the PDF file
        with pymupdf.open(pdf_path) as pdf_document:
            base64_images = []

            # Loop through all pages in the PDF
            for page_num in range(len(pdf_document)):
                # Load the page and generate a pixmap
                page = pdf_document.load_page(page_num)
                pix = page.get_pixmap()

                # Convert pixmap to an image in memory using BytesIO
                image_bytes = io.BytesIO(pix.tobytes())
                img = Image.open(image_bytes)

                # Convert the image to Base64 directly from memory
                base64_image = encode_image_pil(img)
                base64_images.append(base64_image)

            return base64_images

    except Exception as e:
        print(f"Error processing PDF: {e}")
        return []

def encode_image_pil(img: Image.Image) -> str:
    """Encode a PIL image to a Base64 string."""
    with io.BytesIO() as buffer:
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
