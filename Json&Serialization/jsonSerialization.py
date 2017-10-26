# Authot:Bill Lew
import json

info = {'name ': 'Bill',"age ": 22}

with open('test.txt','w')as f:
    # print(pickle.dumps(info))
    f.write(json.dumps(info))
