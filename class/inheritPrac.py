# Author:Bill Lew

class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.students = []
        self.teachers = []
    def enroll(self,obj):
        self.students.append(obj)
        print("为%s办理入校手续" %obj.name)
    def hire(self,obj):
        self.teachers.append(obj)
        print("为%s办理入校手续" %obj.name)
    def showTeachers(self):
        print("Teachers: ",end='')
        for teacher in self.teachers:
            print(teacher.name,' ',end='')
        print("")
    def showStudents(self):
        print("Students: ", end='')
        for student in self.students:
            print(student.name, ' ', end='')
        print("")
class SchoolMember:
    members = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass
class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print("""
            -----------info of Teacher: %s------------
            Name:%s
            Age:%d
            Sex:%s
            Salary:%d
            Course:%s
        """ %(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s will teach you %s" %(self.name,self.course))
class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print("""
            -----------info of Student: %s------------
            Name:%s
            Age:%d
            Sex:%s
            ID:%s
            Grade:%d
        """ %(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_tuition(self,amount):
        print("%s has paid tuition for $%d" %(self.name,amount))

school = School("三峡大学","大学路")

t1 = Teacher("Peter",56,"M",200000,"Linux")
t2 = Teacher("Tom",36,"M",120000,"Society")
school.hire(t1)
school.hire(t2)
s1 = Student("Jim",20,"M","2017331091",1)
s2 = Student("Rose",19,"F","2017331021",1)
s3 = Student("Xupeng",18,"M","2016322231",1)
school.enroll(s1)
school.enroll(s2)
school.enroll(s3)
school.showTeachers()
school.showStudents()
for student in school.students:
    student.pay_tuition(5500)
# t1.tell()
# s3.tell()
