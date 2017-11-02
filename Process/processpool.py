__Author__ = 'Bill Lau'

from multiprocessing import Process,Pool
import time
import os
def Foo(i):
    time.sleep(2)
    print('in process:',os.getpid())
    return i + 100

def Bar(arg):
    print('--->exec done:',arg,os.getpid())

if __name__ == "__main__":
    pool = Pool(3)
    print(os.getpid())
    for i in range(10):
        # pool.apply_async(func=Foo, args=(i,))
        pool.apply_async(func=Foo,args=(i,),callback=Bar)#并行,主进程调用的回调
        # pool.apply(func=Foo, args=(i,))#串行

    print('End')
    pool.close()
    pool.join()#等所有进程结束，必须先close再join