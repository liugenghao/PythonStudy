# Author:Bill Lew

name = input("name;")

age = int(input("age:"))

job = input("job:")

salary = input("salary:")


info = '''
---info of %s-----

Name : %s
Age : %d
Job : %s
Salary : %s

''' %(name,name,age,job,salary)

print(info)