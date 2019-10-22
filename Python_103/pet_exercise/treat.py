class Treat:
    def __init__(self, fullness_bonus=1, happiness_bonus=1):
        self.fullness_bonus=fullness_bonus
        self.happiness_bonus=happiness_bonus
    
    def get_happiness(self):
        return self.happiness_bonus
    
    def get_fullness(self):
        return self.fullness_bonus    
    
class ColdPizza(Treat):
    def __init__(self, fullness=5, happiness=5):
        super().__init__(fullness,happiness)

class Bacon(Treat):
    def __init__(self, fullness=2, happiness=10):
        super().__init__(fullness,happiness)

class VeganSnack(Treat):
    def __init__(self, fullness=1, happiness=1):
        super().__init__(fullness,happiness)