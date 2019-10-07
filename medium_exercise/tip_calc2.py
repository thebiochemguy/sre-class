#Exercise 2: Tip Calculator2

tot=float(input("Total Bill Amount? "))
service=input("Level of service? ")
split=int(input("Split how many ways? "))

tip=0.0

if(service.lower() == "good" ):
    tip=.20*tot
elif(service.lower() == "fair"):
    tip=.15*tot
elif(service.lower() == "bad"):
    tip=.10*tot
else:
    print("I don't recognize that option. ")

tot+=tip
print(f'Tip amount: ${tip:.2f}')
print(f'Total amout: ${tot:.2f}')
if(split>0):
    print(f'Amount per person: ${tot/split:.2f}')
