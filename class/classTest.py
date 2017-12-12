
class Dog:
    def __init__(self, name):
        self.name = name
    def bulk(self):
        print("Dog%s:wangwangwang!" %self.name)

# d1 = Dog("1").bulk()
# d2 = Dog(2).bulk()
# d3 = Dog("3").bulk()


class Role:
    __life_value = 1000
    def __init__(self, name, role, weapon,money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.money = money
    def getLife_value(self):
        return self.__life_value
    def set_life_value(self,life_value):
        self.__life_value = life_value
    def shot(self):
        print("shooting...")
        self.__call()
    def got_shot(self):
        print("ah...,I got shot...")
    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name))
    def __call(self):
        print(self.name)
    def __del__(self):
        print("%s die~!" %self.name)
r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
# r1.set_life_value(1200)
# print(r1.getLife_value())
# print(r2.getLife_value())
r1.shot()
# r2.buy_gun('AK_47')
