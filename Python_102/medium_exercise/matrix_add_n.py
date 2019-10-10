#N size matrix addition
a=[[1,3,4,3],[2,4,5,2]]
b=[[5,2,2,1],[1,0,9,3]]
c=[]

if(len(a)!=len(b)):
    print("Matrix are not the same size")
    quit()

for i in range(len(a)):
    result=[]
    if(len(a[i])!=len(b[i])):
        print("Matrix are not the same size")
        quit()
    for k in range(len(a[i])):
        result.append(a[i][k]+b[i][k])
    c.append(result)

print(c)