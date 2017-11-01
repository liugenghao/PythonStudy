

class BillException(Exception):
    def __init__(self,msg):
        self.message = msg

    # def __str__(self):
    #     return self.message

try:
    raise BillException('我的异常')
except BillException as e:
    print(e)