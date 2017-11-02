import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print('run the thread:%s\n'%n)
    print('---------------------')
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)#进程限制,允许同时5个访问
    for i in range(22):
        t = threading.Thread(target=run,args=(i,))
        t.start()
while threading.active_count() != 1:
    pass
else:
    print('----all threads done----')
