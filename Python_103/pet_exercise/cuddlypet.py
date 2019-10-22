from pet import Pet

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=50, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level=cuddle_level

    def be_alive(self):
        self.fullness-=self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()

    def cuddle(self, other_pet):
        for _ in range(self.cuddle_level):
            other_pet.get_love()