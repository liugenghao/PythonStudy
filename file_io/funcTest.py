# Author:Bill Lew
def func1():
    "test.txt"
    print("in the func1")
    return 0

def func2():
    "test2"
    print("in the func2")

print(func1())
print(func2())


def logger():
    with open('text','a+') as f:
        f.write('end action\n')

def test1():
    print('in the test1...')
    logger()
def test2():
    print('in the test1...')
    logger()
def test3():
    print('in the test1...')
    logger()

def t(x=1,y=2):
    print(x)
    print(y)

# t(3,4)
# t()
t(y=333,x=99)

def t2(*args):
    print(args)
def t3(x,*a):
    print(x)
    print(a)
# t2(1,2,3,4,6,5)
# t2(*[1,2,3,4,5])

# t3("kick",2,"ok",4,5,6)

def t4(**a):
    print(a)
t4(name="刘炳佑",age=29,sex="male")