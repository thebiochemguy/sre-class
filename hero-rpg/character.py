class Character:
    def __init__(self, name, health, power):
        self.name=name
        self.health=health
        self.power=power
    
    def attack(self, enemy):
        if not enemy.alive():
            print(f'{enemy.name} is already dead...')
            return
        enemy.health -= self.power
        print(f'{self.name} does {self.power} damage to {enemy.name}' )
        if not enemy.alive():
            print(f'The {enemy.name} is dead.')

    def alive(self):
        return self.health > 0
    
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
        print() 

class Hero(Character):
    def __init__(self,name):
        super(Hero, self).__init__(name,10,5) 
   
class Goblin(Character):
    def __init__(self,name):
        super(Goblin, self).__init__(name,6,2)

class Zombie(Character):
    def __init__(self,name):
        super(Zombie, self).__init__(name,1,1)

    def alive(self):
        return True
       
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, 1, self.power))
        print()
   