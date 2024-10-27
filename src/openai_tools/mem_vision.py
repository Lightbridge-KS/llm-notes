from typing import List
import pandas as pd


from openai import OpenAI
client = OpenAI()


def get_completions_vision_mem_df(image_prompt: str, 
                                  image_urls: List[str] | None = None, 
                                  base64_images: List[str] | None = None, 
                                  system_prompt: str = "You are a helpful assistant.",
                                  model = "gpt-4o"):
    """Get Vision Completion with Memory
    """
    msg: List[dict[str, str | List]] = []
    mem_vision_df = pd.DataFrame({"user_text": [], "user_image_url": [], "assistant_text": []})
    
    if all([base64_images, image_urls]):
        raise ValueError("Must choose one of: `image_prompt` or `image_urls`")
    
    # If Provided `base64_images`, ignore `image_urls`
    if base64_images:
        image_urls = [f"data:image/png;base64,{base64_image}" for base64_image in base64_images]
    
    for i in range(len(image_urls)):
        
        # Add Image prompt and URL to Memory DF
        mem_vision_df.loc[i] = [image_prompt, image_urls[i], None]
        
        # Convert to user-assistance messages
        msg = _get_messages_user_assistant_text_image(mem_vision_df)
        
        # Generate Response
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                *msg
            ]
        )
        response_text = completion.choices[0].message.content
        # response_text = "Resp: " + image_prompt # For Debug
        
        # Update memory DF
        mem_vision_df.loc[i, "assistant_text"] = response_text 
        
    return mem_vision_df


def _get_messages_user_assistant_text_image(mem_vision_df: pd.DataFrame, image_detail = "high") -> list[dict]:
    """Convert user (text + image) + assistant DataFrame into a list of message dictionaries."""
    
    messages: List[dict[str, str | List]] = []
    for i in range(len(mem_vision_df)):
        
        user_text = mem_vision_df["user_text"][i]
        user_image_url = mem_vision_df["user_image_url"][i]
        assistant_text = mem_vision_df["assistant_text"][i]
        
        if user_text and user_image_url:
            messages.append({"role": "user", 
                             "content": [
                                 {"type": "text", "text": user_text},
                                 {"type": "image_url", "image_url": {"url": user_image_url, "detail": image_detail}}
                             ]})
        if assistant_text:
            messages.append({"role": "assistant", "content": assistant_text})
            
    return messages