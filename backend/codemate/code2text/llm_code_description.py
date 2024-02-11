# Use a pipeline as a high-level helper
import torch
from transformers import pipeline

# Larger chunks do not fit into memory
MAX_ALLOWED_CHUNK_SIZE_FOR_DESCRIPTION = 4000

PROMPT = """
What does the following source code do? Write 1-3 short bullet points only. 

```
%CODE
```

Bullet points: 
""".strip()


def get_pipeline(device: str = "cuda:0"):
    """Create a for text generation"""
    pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta", device=device)
    return pipe


def explain_code(code: str, pipe):
    """Explain the given code using a text-generation pipeline and the given prompt."""
    prompt = PROMPT.replace("%CODE", code)
    result = pipe(
        prompt,
        **{
            "temperature": 0.9,
            "top_p": 0.95,
            "repetition_penalty": 1.2,
            "top_k": 50,
            "max_new_tokens": 1024,
        }
    )
    result_str = result[0]["generated_text"].replace(prompt, "").strip()
    return result_str


if __name__ == "__main__":
    # Mnaully test the pipeline
    print("Has GPU:", torch.cuda.is_available())
    pipe = get_pipeline()
    code = """
class AuthMiddleware:
    async def __call__(self, request: Request, call_next, *args, **kwargs):
        # Get the authorization header
        authorization_header = request.headers.get("Authorization")

        # Ensure the authorization header is present
        if not authorization_header:
            raise HTTPException(status_code=400, detail="Missing auth token")

        # Try to verify the token and get the user
        try:
            # Check if we have the token
            pass
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid auth token")

        # Run the function
        return await call_next(request)
    """.strip()

    print(explain_code(code, pipe))
