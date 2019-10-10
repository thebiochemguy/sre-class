#Only rule im following is if two vowls are next too each other.

examples=['good','cheese','man','spoon']

def findvowel(word):
    a=word.find('aa')
    e=word.find('ee')
    i=word.find('ii')
    o=word.find('oo')
    u=word.find('uu')

    if(a >-1 ):
        return a
    elif(e>-1):
        return e
    elif(i>-1):
        return i
    elif(o>-1):
        return o
    elif(u>-1):
        return u
    else:
        return -1

def changeWord(word):
    more=3
    i=findvowel(word)
    if(i > -1):
        return (word[:i] + word[i]*more + word[i:])
    else:
        return word

modified=[]
for word in examples:
    modified.append(changeWord(word))

print(modified)