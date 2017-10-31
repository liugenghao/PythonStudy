# Authot:Bill Lew
# import json
import pickle
def sayHi(name):
    print("Hello",name)
info = {'name ': 'Bill',"age ": 22,"Hi":sayHi}

with open('test.txt.txt','wb')as f:
    # print(pickle.dumps(info))
    f.write(pickle.dumps(info))
