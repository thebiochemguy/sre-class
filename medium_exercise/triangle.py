#Exercise 5: Print a triangle

h=int(input("How high should the tree be? "))
row_size=2*h-1

for y in range(h+1):
    stars=2*y-1
    for x in range(row_size-stars):
        print(' ', end='')
    for x in range(stars):
        print('*',end=' ')
    print()