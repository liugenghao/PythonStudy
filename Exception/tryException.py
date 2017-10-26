# Authot:Bill Lew
def bulk(self):
    print("%s is bulking" % self.name)
class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d = Dog("JJ")
# choice = input(">>>:").strip()
# getattr(d,choice)
# if hasattr(d,choice):
#     func = getattr(d,choice)
#     func('Chicken')
# else:
#     setattr(d,choice,bulk)
# d.talk(d)
# print(hasattr(d,choice))

names = ['alex','bill']
data = {}

try:
    # data['231']
    # a = names[5]
    open("1.txt")
except Exception as e:
    print(e)
# except KeyError as e:
#     print("没有这个key:",e)
# except IndexError as e:
#     print("数组越界",e)
