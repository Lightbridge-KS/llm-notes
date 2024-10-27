from typing import List
import pandas as pd

from openai import OpenAI
client = OpenAI()


def get_completions_text_mem_df(prompts: List[str], model = "gpt-4o"):
    """Get text completion with memory
    """
    
    mem_df = pd.DataFrame({"user": [], "assistant": []})
    
    for i in range(len(prompts)):
        # Get user text 
        mem_df.loc[i] = [prompts[i], None] 
        # Convert to user-assistance messages 
        msg = _get_messages_user_assistant_text(mem_df)
        # Generate Response
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *msg
            ]
        )
        # response_text = "Resp: " + user_texts[i] # For Debug
        response_text = completion.choices[0].message.content
        # Update memory DF
        mem_df.loc[i, "assistant"] = response_text
        
    return mem_df
    

def _get_messages_user_assistant_text(mem_df: pd.DataFrame, 
                                 user_key = "user", 
                                 assistant_key = "assistant") -> list[dict]:
    """Convert user-assistant DataFrame into a list of message dictionaries."""
    messages = []
    for i in range(len(mem_df)):
        if mem_df[user_key][i]:  # Check if 'user' cell is not empty
            messages.append({"role": user_key, "content": mem_df[user_key][i]})
        if mem_df[assistant_key][i]:  # Check if 'assistant' cell is not empty
            messages.append({"role": assistant_key, "content": mem_df[assistant_key][i]})
    return messages

