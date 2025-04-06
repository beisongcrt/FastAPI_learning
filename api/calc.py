from fastapi import APIRouter
from models.schemas import Counter

router = APIRouter()

@router.post("/", summary="计算两个数的运算结果")
def calc(counter: Counter):
    x, y, op = counter.x, counter.y, counter.op
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        if y == 0:
            return {"error": "除数不能为 0"}
        result = x / y
    else:
        return {"error": "不支持的操作符"}
    return {"result": result}
