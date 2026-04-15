from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import create_db_and_tables
from app.api import exhibits
import os

# lifespan 会在 FastAPI 启动前和关闭后执行逻辑
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时自动创建数据库表（如果不存在）
    create_db_and_tables()
    yield

app = FastAPI(
    title="Mobile API Backend",
    description="轻量级后端，SQLite，媒体文件存本地磁盘",
    version="1.2.0",
    lifespan=lifespan
)

# 挂载静态文件目录，使得 media/ 里的文件可以通过 http://127.0.0.1:8000/media 访问
if not os.path.exists("media"):
    os.makedirs("media/images", exist_ok=True)
    os.makedirs("media/videos", exist_ok=True)

app.mount("/media", StaticFiles(directory="media"), name="media")

# 注册功能模块的路由
app.include_router(exhibits.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Exhibit API! Visit /docs for Swagger UI."}

if __name__ == "__main__":
    import uvicorn
    # host="0.0.0.0" 允许局域网访问
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
