import random

class Character:
    def __init__(self, name, health, power, coins):
        self.name=name
        self.health=health
        self.power=power
        self.coins=coins
    
    def attack(self, enemy):
        if not self.alive():
            print(f'{self.name} is dead')
            return
        if not enemy.alive():
            print(f'{enemy.name} is already dead...')
            return
        enemy.receive_damage(self)
    
    def receive_damage(self, attacker):
        self.health -= attacker.power
        print(f'{self.name} recieved {attacker.power} damage from {attacker.name}')
        if(not self.alive()):
           self.death(attacker)

    def alive(self):
        return self.health > 0

    def death(self, attacker):
        attacker.coins += self.coins
        print(f'{self.name} is dead\n{attacker.name} recieves {self.coins}')

    def print_status(self):
        print("{} has {} health and {} power and {} coins.".format(self.name, self.health, self.power, self.coins))
        print() 

class Hero(Character):
    def __init__(self,name):
        super(Hero, self).__init__(name,10,5,50)

class Knight(Character):
    def __init__(self,name):
        super(Knight,self).__init__(name,100,5,50)

    def attack(self, enemy):
        if not self.alive():
            print(f'{self.name} is dead')
            return
        if not enemy.alive():
            print(f'{enemy.name} is already dead...')
            return
        if random.random() < 0.2:
            print(f'{self.name} doese double damage!!')
            self.power+=self.power*2
            enemy.receive_damage(self)
        else:
            self.power=5
            enemy.receive_damage(self)

class Shadow(Character):
    def __init__(self,name):
        super(Shadow,self).__init__(name,1,5,50)

    def receive_damage(self, attacker):
        if random.random() < 0.1:
            print(f'{self.name} gain 2 points of health')
            self.health-=attacker.power
        else:
            print(f'{self.name} dodge the attack from {attacker.name}')
        if(not self.alive()):
            self.death(attacker)

class Medic(Character):
    def __init__(self,name):
        maxHealth=50
        super(Medic, self).__init__(name,maxHealth,2,50)
    
    def receive_damage(self, attacker):
        self.health -= attacker.power
        print(f'{self.name} recieved {attacker.power} damage from {attacker.power}')

        if random.random() < 0.2:
            print(f'{self.name} gain 2 points of health')
            self.health+=2
        if(not self.alive()):
            self.death(attacker)

class Goblin(Character):
    def __init__(self,name):
        super(Goblin, self).__init__(name,6,2,5)

class Zombie(Character):
    def __init__(self,name):
        super(Zombie, self).__init__(name,1,1,1)

    def receive_damage(self, attacker):
        print(f'{self.name} recieved {attacker.power} damage from {attacker.name}')
       
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, 1, self.power))
        print()
   