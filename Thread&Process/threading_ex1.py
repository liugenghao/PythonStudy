# Author:Bill Lew

import threading
import time
def run(n):
    print('task:',n)
    time.sleep(2)

starttime = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('t%s'%i,))
    t.setDaemon(True)#把当前线程设置为守护线程，主线程无需等待守护线程结束，即可自行结束
    t.start()
    t_objs.append(t)
# t.join()
for t in t_objs:
    t.join()
endtime = time.time()
print("----------")
print("cost:",endtime - starttime)

