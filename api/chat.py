from fastapi import APIRouter
from models.schemas import Message

router = APIRouter()

@router.post("/", summary="提问机器人")
def chat(message: Message):
    return {"answer": f"你说的是：{message.question}"}
