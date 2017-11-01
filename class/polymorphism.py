
class Animal():
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass
    @staticmethod
    def animal_talk(obj):
        obj.talk()
class Dog(Animal):
    '''描述狗'''
    def talk(self):
        print("Woof! Woof!")

class Cat(Animal):
    def talk(self):
        print("Meow! Meow!")
d = Dog(" ")
c = Cat(" ")
Animal.animal_talk(d)
Animal.animal_talk(c)

print(Dog.__doc__)