#Exercise 10: NxN square

n=int(input('How big is the square? '))

for y in range(n):
    print('*', end='')
    for x in range(n-1):
        print('*', end='')
    print('')
