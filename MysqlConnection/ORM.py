__Author__ = 'Bill Lau'
from sqlalchemy import create_engine
from  sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,Enum,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

# engine = create_engine("mysql+pymysql://root:root@localhost/mytest",encoding='utf-8',echo=True)
engine = create_engine("mysql+pymysql://root:root@localhost/mytest",encoding='utf-8')

Base = declarative_base()# 生成ORM基类

class User(Base):
    __tablename__ = 'new_table_test'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "%s.name:%s, password:%s"%(self.id,self.name,self.password)
class Student(Base):
    __tablename__ = 'student'
    stu_id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    age = Column(Integer,nullable=False)
    register_date = Column(DATE,nullable=False)
    sex = Column(Enum('M','F'),nullable=False)

    def __repr__(self):
        return "%s.name:%s, age:%s, register_date:%s, sex:%s"%(self.stu_id,self.name,self.age,self.register_date,self.sex)
class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True)
    day = Column(Integer)
    status = Column(String(32))
    stu_id = Column(Integer,ForeignKey('student.stu_id'))#外键关联
    student = relationship("Student",backref="my_study_record")#外键关联的另一张表的状态，backref可以反查
    def __repr__(self):
        return "%s----->day:%s, status:%s, stu_id:%s"%(self.student.name,self.day,self.status,self.stu_id)
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer,ForeignKey('address.id'))
    shipping_address_id = Column(Integer,ForeignKey('address.id'))

    billing_address = relationship("Address")
    shipping_address = relationship("Address")


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))


# Base.metadata.create_all(engine)#创建表结构

Session_class = sessionmaker(bind=engine)#创建与数据库会话类
Session = Session_class()#数据库会话实例

#插入数据
# user_obj = User(name="Lau",password="111122")
# user_obj2 = User(name="Li",password="415263")
# stu = Student(name='Alex',age=29,register_date='2016-03-09',sex='M')
# stu_reord = StudyRecord(day=3,status='D',stu_id=5)
# stu_reord2 = StudyRecord(day=4,status='D',stu_id=2)
# stu_reord4 = StudyRecord(day=3,status='D',stu_id=7)
# stu_reord5 = StudyRecord(day=3,status='D',stu_id=18)
# stu_reord6 = StudyRecord(day=3,status='D',stu_id=30)
# Session.add(stu_reord)
# Session.add(stu_reord2)
# Session.add(stu_reord4)
# Session.add(stu_reord5)
# Session.add(stu_reord6)
# Session.add(user_obj)
# Session.add(user_obj2)

#查询数据
# result = Session.query(User).filter_by(name='Lau').first()#属性查询
# result = Session.query(User).filter_by(name='Lau').all()#
# result = Session.query(User).filter(User.id > 1).all()#条件查询
# result = Session.query(User).filter(User.id > 1).filter(User.id<3).all()#多条件查询
# result = Session.query(User).filter(User.name.in_(['Li','lau'])).all()
# result = Session.query(User).filter(User.name.in_(['Li','lau'])).all()
# result = Session.query(User).filter(User.name.like('la%')).all()
# result = Session.query(Student).all()
# result = Session.query(Student).filter_by(stu_id=2).first()
# print(result.my_study_record)#外键下所有属性
# result = Session.query(StudyRecord).all()
# result = Session.query(Student).all()
# result = Session.query(Student,Study_record).filter(Student.stu_id == Study_record.id).all()#联合查询1
# result = Session.query(Student).join(Study_record).all()#联合查询2

#分组
# from sqlalchemy import func
# result = Session.query(func.count(User.name),User.name).group_by(User.name).all()


#修改数据
# result.name = 'Bill'
# result.password = 'qqqqqq'


# Session.commit()
# Session.rollback()