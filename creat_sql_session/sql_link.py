from sqlalchemy import create_engine
from sqlalchemy import Column, BigInteger, Text, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#创建数据库连接
engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/lagou_data?charset=utf8")
#操作数据可，创建session
session = sessionmaker(bind=engine)

#声明一个基类，用于创建数据表和新增表项
Base = declarative_base()



'''
创建表
'''
class TestTables(Base):
    __tablename__ = 'test_table'
    id = Column(BigInteger,primary_key=True,autoincrement=True,nullable=True)
    position = Column(String(100), nullable=False)
    province = Column(Text, nullable=False)
#
#
#
# if __name__ == '__main__':
#     LagouTables.metadata.create_all(engine)

'''
往数据库写入数据,索引
'''

session_ = session()

tasttables = TestTables(
    position = 'shenzhen',
    province = 'shanghai'
)
session_.add(tasttables)
session_.commit()

query_info = session_.query(TestTables).filter(TestTables.id == 1).first()