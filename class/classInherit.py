# Author:Bill Lew

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
    def eat(self):
        print("%s is eating" %self.name)
    def talk(self):
        print("%s is talking" %self.name)
    def work(self):
        print("%s is working" %self.name)
class Relation():
    # def __init__(self):
    #     print(self.name)
    def make_friends(self,obj):
        print("%s is making friends with %s" %(self.name,obj.name))
        self.friends.append(obj)
class Man(People,Relation):
    def __init__(self,name,age,power):
        # People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.power = power
class Women(People,Relation):
    def __init__(self,name,age,birthing):
        super(Women, self).__init__(name,age)
        self.birting = birthing
m = Man("Bill",22,"Muscle")
w = Women("Lucy",21,"JJ")
m.make_friends(w)
print(m.friends[0].name)