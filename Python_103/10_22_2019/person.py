class Person: 
    def __init__(self, name, email, phone):
        self.name=name
        self.email=email
        self.phone=phone
    
    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}')

    def __str__(self):
        return f'Name: {self.name}\nEmail:{self.email}\nPhone:{self.phone}'
