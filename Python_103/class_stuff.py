import datetime

class Person:
    def __init__(self, name, surname, birthday, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.address = address
        self.telephone = telephone
        self.email = email
    
    def age(self):
        today=datetime.date.today()
        age=today.year - self.birthday.month
        if(today < datetime.date(today.year, self.birthday.month, self.birthday.year)):
            age -= 1
    
        return age


person = Person("Jane","Doe", datetime.date(1992,3,12), "Short Street","555 456 0987","jane.doe@nowhere.com")
print(person.age())