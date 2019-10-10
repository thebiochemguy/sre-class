#Multiply vectors

a=[22,4,5]
b=[2,3,6]

if(len(a) != len(b)):
    print('Vector Multiplication cant happen')
    quit()

c=[]

for i in range(len(a)):
    c.append(a[i]*b[i])

print(f'{a} x {b} = {c}')
