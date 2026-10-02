from fastapi import FastAPI
from pydantic import BaseModel, Field
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title="AI Assistant API",
    version="1.0.0"
)


class AIRequest(BaseModel):
    prompt: str = Field(min_length=1)
    temperature: float = Field(
        default=0.7,
        ge=0.0,
        le=2.0
    )
    max_tokens: int = Field(
        default=100,
        ge=1,
        le=4000
    )


@app.get("/")
def home():
    logger.info("Health check endpoint called")

    return {
        "status": "running",
        "message": "AI Assistant API is working"
    }


@app.get("/about")
def about():
    logger.info("About endpoint called")

    return {
        "project": "AI Assistant API",
        "version": "1.0.0",
        "developer": "Vishnumurthy",
        "technology": "FastAPI"
    }


@app.post("/generate")
def generate(request: AIRequest):

    logger.info("AI generation request received")

    try:
        logger.info(
            "Prompt length: %d",
            len(request.prompt)
        )

        response = f"AI response for: {request.prompt}"

        logger.info("AI response generated successfully")

        return {
            "prompt": request.prompt,
            "response": response,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens
        }

    except Exception:
        logger.exception("AI generation failed")

        return {
            "error": "AI generation failed"
        }