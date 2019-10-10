#Leet speek 
#Translates To
#A 	4
#E 	3
#G 	6
#I 	1
#O 	0
#S 	5
#T 	7
#

s="I am a leet programmer"
leet=""
for i in s:
    if(i.upper()=='A'):
        leet+='4'
    elif(i.upper()=='E'):
        leet+='3'
    elif(i.upper()=='G'):
        leet+='6'
    elif(i.upper()=='I'):
        leet+='1'
    elif(i.upper()=='O'):
        leet+='0'
    elif(i.upper()=='S'):
        leet+='5'
    elif(i.upper()=='T'):
        leet+='7'
    else:
        leet+=i

print(leet)
