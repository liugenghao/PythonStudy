__Author__ = 'Bill Lau'

import pymysql

#创建连接
conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='mytest')
#创建游标
cursor = conn.cursor()

#执行SQL，并返回收影响行数
# effect_row = cursor.execute('select * from student')
# print(cursor.fetchall())

data = [
    ("N1",22,'2015-02-03','M'),
    ("N2", 22, '2015-02-03', 'F'),
    ("N3", 22, '2015-02-03', 'M'),
    ("N4", 22, '2015-02-03', 'F')
]
#插入数据
# cursor.executemany('insert into student(name,age,register_date,sex) values(%s,%s,%s,%s)',data)
# conn.commit()

#删除
# cursor.execute('delete from student where stu_id > 18 and stu_id <29')

cursor.close()
conn.close()