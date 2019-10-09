#exercise 8: N to M

N=int(input("Please enter a number to start with: "))
M=int(input("What number shall we end on: "))


while(N != M):
    print(f'{N}')
    if( N < M):
        N+=1
    elif( N > M):
        N-=1

print(f'{N}')

