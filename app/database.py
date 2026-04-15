from sqlmodel import SQLModel, create_engine, Session

# 本地 SQLite 数据库文件名称
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# 对于 SQLite 来说这个配置是必须的，以防不同线程的错误
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    """根据模型创建数据库表"""
    SQLModel.metadata.create_all(engine)

def get_session():
    """获取数据库会话，用于依赖注入"""
    with Session(engine) as session:
        yield session
