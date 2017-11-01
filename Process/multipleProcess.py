import multiprocessing,time,threading
def run_threading():
    print(threading.get_ident())
def run(name):
    time.sleep(2)
    print("hello,",name)
    threading.Thread(target=run_threading).start()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('Lew %s'%i,))
        p.start()

