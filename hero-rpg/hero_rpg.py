#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import character

main_menu = [   
    "Fight Goblin",
    "Fight Zombie",
    "do nothing",
    "Print hero status",
    "Print goblin status",
    "Print zombie status",
    "flee",
]

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

def choices_to_string(choice_list):
    choice_string = ""
    num=1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num+=1
    choice_string += "Please choose an option: "
    return choice_string

def print_menu_error():
    print("That was not a vaild choice. Try again.\n\n\n")

def badDude_turn():
    if bad_dude.alive():
        bad_dude.attack(dude)
    if bad_dude2.alive():
        bad_dude2.attack(dude)

dude=character.Hero("Hero")
bad_dude=character.Goblin("Goblin")
bad_dude2=character.Zombie("Zombie")

def main():

    while (bad_dude.alive() or bad_dude2.alive()) and dude.alive():
        
        raw_input=get_user_choice(main_menu)
        if raw_input == 1:
            dude.attack(bad_dude)
            badDude_turn()         
        elif raw_input == 2:
            dude.attack(bad_dude2)
            badDude_turn()
        elif raw_input == 3:
            badDude_turn()
        elif raw_input == 4:
            dude.print_status()
        elif raw_input == 5:
            bad_dude.print_status()
        elif raw_input == 6: 
            bad_dude2.print_status()
        elif raw_input == 7:
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        
        if not dude.alive:
            print("You are dead.")

main()
