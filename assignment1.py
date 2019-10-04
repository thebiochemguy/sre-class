l_name_s=0
l_name_f=0

while l_name_s == 0 or l_name_f == 0:
    if l_name_s == 0:
        name_s=input("What is your name: ")
        l_name_s=len(name_s)
    if l_name_f == 0:
        name_f=input("What is your friends name: ")
        l_name_f=len(name_f)

greeting = f'Hello {name_s}, it is very nice to meet you and your friend {name_f}'
print(greeting)