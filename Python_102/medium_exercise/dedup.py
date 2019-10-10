#dedup exercise

a=[1,2,4,5,1,2,4,1,2,3,5,2,1,'a','b','c','a',100,'d',100,'boo','boo','cat','cat','dog']

unique=[]

for i in a:
     if( i not in unique):
         unique.append(i)

print(unique)
