class MyType(type):
    def __init__(self,what,bases=None,dict=None):
        print("--MyType init---")
        super(MyType,self).__init__(what,bases,dict)
    def __call__(self, *args, **kwargs):
        print("--MyType Call---")
        obj = self.__new__(self,*args,**kwargs)
        self.__init__(obj,*args,**kwargs)

class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("Foo ---init__")
    def __new__(cls, *args, **kwargs):
        print("Foo ---new---")
        return object.__new__(cls)


obj = Foo('Bill')
print(obj.name)