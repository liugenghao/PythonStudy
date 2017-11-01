a = ((i*2 for i in range(10)))
# print(a.__next__())
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print('|',b,end='')
        yield b #生成器关键字
        a, b = b ,a+b
        '''
        t = (b,a+b)
        a = t[0]
        b = t[1]
        '''
        n = n + 1
    return 'done'

f = fib(8)
print(f)
print("startform".center(30,"-"))
while True:
    try:
        x = next(f)
        print('f:',x,'|',end='')
    except StopIteration as e:
        print('\nGenerator return value',e.value)
        break