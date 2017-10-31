# Author:Bill Lew

import threading
import time
def run(n):
    print('task:',n)
    time.sleep(2)

starttime = time.time()
# t_obj = []
for i in range(50):
    t = threading.Thread(target=run,args=('t%s'%i,))
    t.start()
    # t_obj.append(t)
t.join()
# for t in t_obj:
#     t.join()
endtime = time.time()
print("----------")
print("cost:",endtime - starttime)

