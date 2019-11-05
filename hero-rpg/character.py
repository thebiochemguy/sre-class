class Character:
    def __init__(self, health, power):
        self.health=health
        self.power=power

class Hero(Character):
    def __init__(self):
        super(Hero, self).__init__(10,5)

class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__(6,2)