from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import List
from app.database import get_session
from app.models import Exhibit

router = APIRouter(prefix="/exhibits", tags=["Exhibits"])

@router.post("/", response_model=Exhibit)
def create_exhibit(exhibit: Exhibit, session: Session = Depends(get_session)):
    """创建一个新的展品内容"""
    session.add(exhibit)
    session.commit()
    session.refresh(exhibit)
    return exhibit

@router.get("/", response_model=List[Exhibit])
def read_exhibits(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    """分页读取所有展品信息"""
    exhibits = session.exec(select(Exhibit).offset(skip).limit(limit)).all()
    return exhibits
