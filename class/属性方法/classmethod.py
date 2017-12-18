__Author__ = "Bill Lau"
class Game():
    num =0
    def __init__(self):
        self.name = 'Jim'

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100

game = Game()
Game.add_num()
print(game.num)