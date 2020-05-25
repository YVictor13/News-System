from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

engine = create_engine('mysql://root:123456@localhost/newsystem?charset=utf8')
Base = declarative_base()


class News(Base):
    # 新闻类型
    __tablename__='news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)

# 创建表格
Base.metadata.create_all(engine)