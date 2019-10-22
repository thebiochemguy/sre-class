class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name=name
        self.fullness=fullness
        self.happiness=happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys=[]

    def eat_food(self):
        self.fullness+=30
    
    def get_love(self):
        self.happiness+=30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness+=toy.use()

    def get_toy(self, toy):
        self.toys.append(toy)

    def get_treat(self,fullness,happiness):
        self.fullness+=fullness
        self.happiness+=happiness 

    def __str__(self):
        return f'''
        { self.name }
        Fullness: {self.fullness}
        Happiness: {self.happiness}
        ''' 


