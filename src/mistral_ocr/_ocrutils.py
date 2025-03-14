import base64
from pathlib import Path


def replace_images_in_markdown(markdown_str: str, images_dict: dict) -> str:
    for img_name, base64_str in images_dict.items():
        markdown_str = markdown_str.replace(
            f"![{img_name}]({img_name})", f"![{img_name}]({base64_str})"
        )
    return markdown_str


def save_base64_to_image(base64_string, output_file_path):
    """
    Save a base64 encoded image string to an image file.
    """
    try:
        # If the base64 string contains the MIME type prefix, remove it
        if "base64," in base64_string:
            base64_string = base64_string.split("base64,")[1]
        
        # Decode the base64 string
        img_data = base64.b64decode(base64_string)
        
        # Write the binary data to a file
        with open(Path(output_file_path), "wb") as f:
            f.write(img_data)
            
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False