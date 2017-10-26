# Author:Bill Lew
class A:
    def __init__(self):
        print("A")
class B(A):
    # def __init__(self):
    #     print("B")
    pass
class C(A):
    # def __init__(self):
    #     print("C")
    pass
class D(B,C):
    pass

D()