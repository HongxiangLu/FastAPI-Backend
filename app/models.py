from typing import Optional
from sqlmodel import Field, SQLModel

class Exhibit(SQLModel, table=True):
    """展品内容模型"""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str  # 展品描述文字
    image_url: Optional[str] = None  # 展品图片存储在本地 media/images 的相对路径或下载 URL
    video_url: Optional[str] = None  # 展品视频存储在本地 media/videos 的相对路径或下载 URL
