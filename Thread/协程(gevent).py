__Author__ = 'Bill Lau'
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')
def func3():
    print('Running in func3')
    gevent.sleep(0)
    print('print func3 again')

gevent.joinall([gevent.spawn(foo),gevent.spawn(bar),gevent.spawn(func3)])