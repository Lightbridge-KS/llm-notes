import base64
import re
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
    

def add_image_folder_in_markdown(markdown_string, folder_path=Path(".")):
    """
    Add a folder path before image filenames in markdown image links.
    """
    # Validate that folder_path is a Path object
    if not isinstance(folder_path, Path):
        raise TypeError("folder_path must be a pathlib.Path object")
    
    # Ensure the folder path ends with a separator
    # Path.as_posix() converts the path to a string with forward slashes
    # We add a trailing slash if it doesn't already have one
    folder_str = folder_path.as_posix()
    if not folder_str.endswith('/'):
        folder_str += '/'
    
    # Pattern matches markdown image syntax: ![alt](filename)
    pattern = r'(!\[.*?\])\((.*?)\)'
    
    # Replace function adds the folder path to the filename part
    def add_folder(match):
        alt_text = match.group(1)
        filename = match.group(2)
        return f'{alt_text}({folder_str}{filename})'
    
    # Apply the replacement
    return re.sub(pattern, add_folder, markdown_string)