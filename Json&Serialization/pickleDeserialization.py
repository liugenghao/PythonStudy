
import pickle
def sayHi(name):
    print("Hello!",name)
with open("test.txt.txt",'rb')as f:
    # data = pickle.loads(f.read())
    # data = pickle.loads(f.read())
    data = pickle.load(f)
    count = 0
    for i in data:
        if count == 2:
            print(i,data[i]("Bill"))
        else:
            print(i,data[i])
        count += 1
