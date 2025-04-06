from fastapi import FastAPI
from api import chat, calc

app = FastAPI(
    title="迷你 API 项目",
    description="这是一个支持聊天、计算的练习项目。",
    version="1.0.0"
)

# 注册功能模块路由
app.include_router(chat.router, prefix="/chat", tags=["聊天功能"])
app.include_router(calc.router, prefix="/calc", tags=["计算功能"])
