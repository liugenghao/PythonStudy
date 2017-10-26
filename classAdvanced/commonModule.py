# Authot:Bill Lew

class C:
    '''C class'''
    def __init__(self):
        self.name = 'Bill'
        self.data = {}
    def __call__(self, *args, **kwargs):
        print("call function",args,kwargs)
    def __str__(self):
        return "<__str__----obj:%s>" %self.name
    def __setitem__(self, key, value):
        print("__setitem__",key,value)
        self.data[key] = value
    def __getitem__(self,key):
        print("__getitem__",key)
        return self.data.get(key)
    def __delitem__(self, key):
        print("delete dataitem:",key)
        del self.data[key]

obj = C()
# obj()
# obj(1,2,3,name=123)
# print(C.__dict__)
# print(C.__doc__)
print(obj)
# obj['name'] = 'Lew'
# obj['name']
# del obj['name']
# print(obj['name'])