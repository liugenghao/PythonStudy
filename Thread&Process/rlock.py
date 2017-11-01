# Authot:Bill Lew
import threading
num1,num2 = 0 ,0
lock = threading.RLock()#递归锁
def run1():
    print('grab the first part data')
    lock.acquire()
    global num1
    num1 += 1
    lock.release()
    return num1
def run2():
    print('grab the second part data')
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2
def run3():
    lock.acquire()
    res1 = run1()
    print('-----between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res1,res2)
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done----')
    print("num1:%s,num2:%s"%(num1,num2))
