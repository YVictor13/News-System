from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123456@localhost/newsystem?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class News(Base):
    # 新闻类型
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(2000), nullable=False)
    types = Column(String(10), nullable=False)
    image = Column(String(300))
    author = Column(String(20))
    view_count = Column(Integer)
    created_at = Column(DateTime)
    is_valid = Column(Boolean)


#
# # 创建表格
# Base.metadata.create_all(engine)

class OrmTest(object):

    def __init__(self):
        self.session = Session()

    # 新增一条记录
    def add_one(self):
        new_obj = News(
            title='title',
            content='content',
            types='百家'
        )
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    # 新增多条数据，使用[]进行包裹，成为数组
    def add_all(self):
        self.session.add_all([
            News(title='title', content='hah', types='good'),
            News(title='xhx', content='xixi', types='base')]
        )
        self.session.commit()

    # 查询数据
    def get_one(self):
        return self.session.query(News).get(1)

    # 查询多条数据
    def get_more(self):
        return self.session.query(News).filter_by(title='title')


def main():
    obj = OrmTest()
    # res = obj.add_all()
    # print(res)
    res = obj.get_more()
    for item in res:
        print(item)


if __name__ == '__main__':
    main()
