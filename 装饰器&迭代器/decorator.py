#迭代器
import time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("function cost %s" %(end_time - start_time))
    return deco
@timer
def foo1():
    time.sleep(2)
    print("in the foo1")

@timer
def foo2(name,age):
    time.sleep(1)
    print("in the foo2",name,age)
foo1()
foo2("Alex",22)