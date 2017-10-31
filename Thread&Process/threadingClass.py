# Author:Bill Lew
import threading,time
class MyTread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyTread,self).__init__()
        self.n = n
        self.sleep_time = sleep_time

    def run(self):
        print("running task:%s,sleep %s second"%(self.n,self.sleep_time))
        time.sleep(self.sleep_time)


t1 = MyTread('t1',2)
t2 = MyTread('t2',4)
t3 = MyTread('t3',6)

t1.start()
t2.start()
t2.join()
t3.start()

