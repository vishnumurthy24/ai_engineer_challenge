from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class AIRequest(BaseModel):
    prompt: str = Field(min_length=1)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=100, ge=1, le=4000)


@app.get("/")
def home():
    return {
        "message": "AI API is running"
    }


@app.post("/generate")
def generate(request: AIRequest):
    response = f"AI response for: {request.prompt}"

    return {
        "prompt": request.prompt,
        "response": response,
        "temperature": request.temperature,
        "max_tokens": request.max_tokens
    }