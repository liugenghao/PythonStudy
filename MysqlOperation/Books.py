__Author__ = "Bill Lau"
from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,Enum,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship,mapper

# engine = create_engine("mysql+pymysql://root:root@localhost/mytest",encoding='utf-8',echo=True)
engine = create_engine("mysql+pymysql://root:root@localhost/books?charset=utf8",encoding='utf-8')

Base = declarative_base(engine)# 生成ORM基类

book_m2m_author = Table('book_m2m_author',Base.metadata,#生成多对多关系表
                        Column('book_id',Integer,ForeignKey('book.id')),
                        Column('author_id',Integer,ForeignKey('author.id')))

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    email = Column(String(32))
    books = relationship('Book',secondary=book_m2m_author,backref="books")#关联映射关系

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref="authors")

    def __repr__(self):
        return self.name
# Base.metadata.create_all(engine)#创建表结构

Session_class = sessionmaker(bind=engine)#创建与数据库会话类
Session = Session_class()#数据库会话实例


# book1 = Book(name='Learning Python',pub_date='2015-10-01')
# book2 = Book(name='Have funning',pub_date='2013-08-23')
# book3 = Book(name='Release Peace',pub_date='2016-03-11')
#
# author1 = Author(name="Bill Lau",email="bill@foxmail.com")
# author2 = Author(name="Alex Wang",email="Alex@sina.com")
# author3 = Author(name="Jack Wu",email="Jack@sohu.com")
#
# book1.authors = [author1,author3]
# book2.authors = [author1]
# book3.authors = [author1,author2,author3]
# Session.add_all([book1,book2,book3,author1,author2,author3])

result = Session.query(Author).filter_by(name="Bill Lau").first()
print(result.books)
# Session.commit()