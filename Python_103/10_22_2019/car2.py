class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def print_info(self):
        print(f'{self.year} {self.make} {self.model}')

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mpg):
        super(Motorcycle, self).__init__(make,model,year)
        self.mpg=mpg

    def print_info(self):
        print(f'Motorcycle: {self.year} {self.make} {self.model}')


car=Vehicle('Nissan','Leaf',2015)
car.print_info()
bike=Motorcycle("Harley","Hog","1966",50)
bike.print_info()