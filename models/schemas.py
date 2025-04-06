from pydantic import BaseModel, Field

class Message(BaseModel):
    question: str = Field(..., example="你是谁？", description="用户输入的问题")

class Counter(BaseModel):
    x: int
    y: int
    op: str = Field(..., description="操作符，仅支持 + - * /", pattern=r"^[+\-*/]$")
