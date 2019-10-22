class Car:
    def __init__(self, color, name, model):
        self.color=color
        self.name=name
        self.model=model

class Electric(Car):
    def details(self):
        print(f'Electric car')

car1=Car("Green","Honda","civic")
car2=Electric("Blue","Telsa","Model3")

print(car1.name)
print(car2.name)
car2.details()
