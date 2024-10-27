from openai import OpenAI
client = OpenAI()


def get_completions_text(prompt: str,
                         system: str = "You are a helpful assistant.",
                         model: str = "gpt-4o"):
    
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    text = completion.choices[0].message.content
    return text
