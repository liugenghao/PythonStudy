import time
import threading

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if count > 4 and count < 10:#改成红灯
            event.clear()#清空标志位
            print("\033[41;1mred light is on...\033[0m")
        elif count > 11:
            event.set()#变绿灯
            count = 0
        else:
            print('\033[42;1mgreen light is on...\033[0m')
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():#绿灯
            print("[%s] running...."%name)
            time.sleep(1)
        else:
            print("[%s] stop and wait...."%name)
            event.wait()
            print("[%s] start going...."%name)

light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car,args=('teslar',))
car.start()