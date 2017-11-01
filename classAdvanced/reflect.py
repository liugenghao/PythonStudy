def bulk(self):
    print("%s is bulking" % self.name)
class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("%s is eating %s" %(self.name,food))

d = Dog("JJ")
choice = input(">>>:").strip()
if hasattr(d,choice):#判断是对象中否有choice方法名
    func = getattr(d,choice)
    func('Chicken')#调用该方法
else:
    setattr(d,choice,bulk)
d.talk(d)
# print(hasattr(d,choice))