#exercise 3" Coins

coins=0
ans=""

while(ans.lower() != "no"):
    #print(f'You have {coins} coins.')
    ans=input(f"You have {coins} coins.\nDo you want another? ")
    if(ans.lower() == "no" or ans.lower() == "yes"):
        coins+=1

print("Bye")