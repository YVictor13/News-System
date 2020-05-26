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
        return self.session.query(News).filter_by(title="title")

    # 修改数据
    def update_data(self, id):
        obj = self.session.query(News).get(id)
        if obj:
            obj.title = 'shdh'
            self.session.add(obj)
            self.session.commit()
            return obj
        # return False

    # 修改多条数据
    def update_data_more(self):
        data_list = self.session.query(News).filter_by(title='title')
        for item in data_list:
            item.is_valid = 1
            self.session.add(item)
        self.session.commit()
        return data_list

    # 删除单条数据
    def delete_data(self, id):
        # 获取需要删除的数据
        obj = self.session.query(News).get(id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False

    # 删除多条数据
    def delete_data_more(self, id):
        data_list = self.session.query(News).filter(News.id > id)
        if data_list:
            for item in data_list:
                if item:
                    self.session.delete(item)
                    self.session.commit()

            return True
        return False


def main():
    obj = OrmTest()
    # res = obj.add_all()
    # print(res)
    # res = obj.get_more()
    # print(res)
    # # for item in res:
    # #     print(item)
    # res = obj.get_more()
    # for item in res:
    #     print("id:%s" % item.id, "title:%s" % item.title)
    # 测试更新功能

    # res = obj.update_data(3)
    # print(res.title,res.id)

    # res = obj.update_data_more()
    # for item in res:
    #     print(item.id,item.is_valid)

    # 测试删除功能
    obj.delete_data_more(3)


if __name__ == '__main__':
    main()
