#Matrix Addition 2x2

a=[[1,3],[2,4]]
b=[[5,2],[1,0]]
c=[]

if(len(a)!=len(b)):
    print("Matrix are not the same size")
    quit()

for i in range(len(a)):
    result=[]
    for k in range(len(a[i])):
        result.append(a[i][k]+b[i][k])
    c.append(result)

print(c)