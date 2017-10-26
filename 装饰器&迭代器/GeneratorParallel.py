# Authot:Bill Lew
import time
def consumer(name):
    print("【%s】准备吃包子了" %name)
    while True:
        baozi = yield
        print("包子【%s】来了，被【%s】吃了" %(baozi,name))

def producer():
    c = consumer("嘟嘟嘟")
    c2 = consumer("小红")
    c.__next__()
    c2.__next__()
    print("我要开始做包子了！")
    for i in range(10):
        time.sleep(1)
        print("制作了包子[",i,"]，分成两半")
        c.send(i)
        c2.send(i)

producer()