

def add(a,b,f):
    return f(a)+f(b)


def f(x):
    if x >= 0:
        return x
    else:
        return -x
res = add(3,-6,f)
print(res)