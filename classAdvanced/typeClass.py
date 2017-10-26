# Authot:Bill Lew
def func(self):
    '''type为类的类'''
    print("hello,",self.name)
def __init__(self,name,age):
    self.name = name
    self.age = age
Foo = type('Foo',(),{'talk':func,'__init__':__init__})
f = Foo('Bill',23)
f.talk()