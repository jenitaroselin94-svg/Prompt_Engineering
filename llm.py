import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
load_dotenv()
MODEL = "Qwen/Qwen2.5-72B-Instruct"
def generate_response(prompt, temperature=0.3, max_tokens=500):
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        raise RuntimeError(
            "HF_TOKEN is missing. Please set your "
            "Hugging Face API token."
        )
    client = InferenceClient(
        api_key=hf_token
    )
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an educational AI assistant. "
                    "Provide clear, useful and accurate "
                    "answers for college students."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

