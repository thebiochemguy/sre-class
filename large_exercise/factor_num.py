#exercise 2: find the factors

num=int(input("Please input the number to factor: "))

for i in range(1,num+1):
    if( num % i == 0):
        print(f'{i}',end=' ')

print()
