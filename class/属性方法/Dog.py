import abc
class Dog:
    def __init__(self,name,food):
        self.name = name
        self.__food = food
    @property
    def eat(self):#属性方法不能直接删除
        print("%s is eating" %self.name)

    @eat.setter
    def eat(self,food):
        print("set the food",food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print("私有变量删除")

    @abc.abstractmethod
    def go(self):pass

d = Dog("JJ","Mantou")
# d.eat()
d.eat
d.eat = 'Baozi'