from pet import Pet
from cuddlypet import CuddlyPet
from toy import Toy
from treat import ColdPizza

pets=[]

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Give pet a treat",
    "Do nothing",
]

adoption_menu=[
    "Pet",
    "Cuddly Pet"
]

treat_menu=[
    "Cold Pizza",
    "Bacon",
    "VeganSnack",
]

def print_menu_error():
    print("That was not a vaild choice. Try again.\n\n\n")

def choices_to_string(choice_list):
    choice_string = ""
    num=1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num+=1
    choice_string += "Please choose an option: "
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

def main():
    while True:
        choice=get_user_choice(main_menu)
        if choice == 1:
            pet_name=input("What is your pets name? ")
            print("Please choose the type of pet:")
            type_choice=get_user_choice(adoption_menu)
            if type_choice==1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print(f'You now have {len(pets)} pets')
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            for pet in pets:
                pet.eat_food()
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                t=Toy()
                pet.get_toy(t)
        if choice == 6:
            type_choice=get_user_choice(treat_menu)
            if type_choice==1:
               f=ColdPizza().get_fullness()
               h=ColdPizza().get_happiness()
            if type_choice ==2:
                f=Bacon().get_fullness()
                h=Bacon().get_happiness()
            if type_chose == 3:
                f=VeganSnack().get_fullness()
                h=VeganSnack().get_happiness()
            
            for pet in pets:
                pet.get_treat(f,h)
            
        if choice == 7:
            for pet in pets:
                pet.be_alive()

main()
