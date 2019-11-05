#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import character

dude=character.Hero()
bad_dude=character.Goblin()

def main():
#    hero_health = dude.health
#    hero_power = dude.power
#    goblin_health = bad_dude.health
#    goblin_power = bad_dude.power


    while bad_dude.health > 0 and dude.health > 0:
        print("You have {} health and {} power.".format(dude.health, dude.power))
        print("The goblin has {} health and {} power.".format(bad_dude.health, bad_dude.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            bad_dude.health -= dude.power
            print("You do {} damage to the goblin.".format(dude.power))
            if bad_dude.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if bad_dude.health > 0:
            # Goblin attacks hero
            dude.health -= bad_dude.power
            print("The goblin does {} damage to you.".format(bad_dude.power))
            if dude.health <= 0:
                print("You are dead.")


main()
