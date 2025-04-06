# 文件名：start.py
import uvicorn
import config

def main():
    uvicorn.run(
        config.APP_IMPORT,
        host=config.HOST,
        port=config.PORT,
        reload=config.RELOAD,
        workers=config.WORKERS
    )

if __name__ == "__main__":
    print("🌟 正在启动 FastAPI 应用...")
    main()
