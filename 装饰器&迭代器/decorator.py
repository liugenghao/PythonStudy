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
# foo1()
# foo2("Alex",22)

from time import ctime, sleep

def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappedfunc():
            print("%s called at %s %s"%(func.__name__, ctime(), pre))
            return func()
        return wrappedfunc
    return timefun

@timefun_arg("itcast")
def foo():
    print("I am foo")

@timefun_arg("python")
def too():
    print("I am too")

foo()
sleep(2)
foo()

too()
sleep(2)
too()