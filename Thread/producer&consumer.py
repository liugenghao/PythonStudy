import threading, queue, time
q = queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True:
        time.sleep(0.1)
        q.put('骨头%s'%count)
        count += 1
        print('生产了骨头',count)

def Consumer(name):
    while True:
        print("[%s]取到了{%s}并且吃了它"%(name,q.get()))
        time.sleep(1)


p = threading.Thread(target=Producer,args=('Alex',))
c = threading.Thread(target=Consumer,args=('xiao K',))
c2 = threading.Thread(target=Consumer,args=('da J',))

p.start()
c.start()
c2.start()