from fastapi import APIRouter

router = APIRouter()

# @router.get("/", summary="欢迎页")
# def root():
#     return {
#         "message": "欢迎使用迷你 AI 工具箱",
#         "docs": "/docs",
#         "status": "online"
#     }


from fastapi.responses import RedirectResponse

@router.get("/", include_in_schema=False)  # 不显示在 docs 页面
def root_redirect():
    return RedirectResponse(url="/docs")
