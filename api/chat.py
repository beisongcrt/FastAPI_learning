from fastapi import APIRouter
from models.schemas import Message

router = APIRouter()

@router.get("/")  # 装饰器，定义了一个 HTTP GET 请求路由，路径为根路径 "/"
def read_root():  # 定义处理该路由的函数
    return {"message": "你好，这是根路径"}  # 返回 JSON 响应

@router.post("/", summary="提问机器人")
def chat(message: Message):
    return {"answer": f"你说的是：{message.question}"}
