#!/usr/bin/env python

# In this secon part of the simple RPG game, with some changes. the options are to:

# 1. fight 
# 2. do nothing - in which case the enimes will attack anyway
# 3. print heros status, too see heath and coins
# 4. see enemies status, see enemies health
# 5. flee

import character
import random

main_menu = [   
    "fight",
    "do nothing",
    "Print heros status",
    "See enemies status",
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

def get_victim(group):
    vict=random.randint(0,len(group)-1)
    while not group[vict].alive():
        vict=random.randint(0,len(group)-1)
    return group[vict]

def group_alive(group):
    for member in group:
        if(member.alive()):
            return True
    return False

def fight(attacker,defender):
    for a in attacker:
        a.attack(get_victim(defender))

def get_status(group):
    for actor in group:
        actor.print_status()

hero=character.Knight("Hero")
goblin=character.Goblin("Goblin")
zombie=character.Zombie("Zombie")
medic=character.Medic("Medic")
shadow=character.Shadow("Shadow")

good_guys=[hero,medic,shadow]
bad_guys=[goblin,zombie]

def main():
    while (group_alive(good_guys) and group_alive(bad_guys)):
        raw_input=get_user_choice(main_menu)
        if raw_input == 1:  #Hero attacks random enemy
            fight(good_guys,bad_guys)
            fight(bad_guys,good_guys)         
        elif raw_input == 2:  #Does nothing but bad guys still attack
            fight(bad_guys,good_guys)
        elif raw_input == 3:  #Get status of hero
            get_status(good_guys)  
        elif raw_input == 4:  #get Status of enemies
            get_status(bad_guys)
        elif raw_input == 5:  #Run away
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        

        # if not dude.alive:
        # print("You are dead.")

main()
