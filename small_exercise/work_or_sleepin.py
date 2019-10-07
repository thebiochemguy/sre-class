#Exercise 5

day=int(input("Day (0-6)? "))

if(day==0 or day==6):
    print(f'Sleep in')
elif (day > 6 or day < 0):
    print(f'Invalid day, do whatever... ')
else:
    print(f'Go to work')