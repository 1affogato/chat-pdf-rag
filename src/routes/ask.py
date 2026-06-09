from fastapi import APIRouter
from pydantic import BaseModel

from src.services.rag_service import ask_rag

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(data: QuestionRequest):

    answer = ask_rag(
        data.question
    )

    return {
        "answer": answer
    }