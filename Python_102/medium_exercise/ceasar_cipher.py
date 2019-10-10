#Caesar cipher e(x)=(x-k)(mod 26)

k=13

alpha="abcdefghijklmnopqrstuvwxyz"
mesg="lbh zhfg hayrnea jung lbh unir yrnearq"

decrypt=""

for c in mesg:
    if(c == " "):
        decrypt+=' '
    else:
        i=(alpha.find(c)+k)%26
        decrypt+=alpha[i]

print(decrypt)
        
