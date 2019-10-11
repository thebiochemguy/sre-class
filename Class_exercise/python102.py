#mylist=["horse","chicken","goat"]

# print(mylist)
# print(mylist[0])

# mylist[0]="cat"

# print(f'Here are my animals {mylist[0]}')

# todos=["Pet the cat","Goto sleep"]
# print(todos)
# todos.append("Watch tv")
# print(todos)
# count=0
# while count < len(todos):
#     print(f'{todos[count]}')
#     count+=1

# todos = todos+["Feed the dog", True ,"Let cat out"]

# del todos[5]
# print(todos)

# stuff=[]

# while True:
#     item=input("What needs to be done today? ")
#     if(item==""):
#         break
#     stuff.append(item)
#     print(f'Here is your current todo: {stuff}')

# print(f"Exited: Here are your todo items\n{stuff}")

# numbers = [1, 2,3,4,5,6,7]
# numbers.insert(3,True)
# print(numbers)

# print(numbers.pop())
# print(numbers)
# new_numbers=numbers
# print(f'numbers{numbers}')
# print(f'new_numbers {new_numbers}')

# new_numbers=numbers.copy()
# new_numbers[0]=99

# print(f'numbers{numbers}')
# print(f'new_numbers {new_numbers}')

# for i in range(10):
#     print(i)
# 
# for m in range(11):
#     for n in range(11):
#         print(f'{m} x {n} = {m*n}')

# def s():
#     print('********')

# def getGroceries():
#     print('milk')
#     s()
#     print("cheese")
#     s()
#     print("eggs")



# getGroceries()

# def add(x,y):
#     print(x+y)

# def hello(name):
#     print("Hello "+name)

# hello("juan")
# hello("Alim")

# add(2,5)

def c_to_f(f):

    return (int(f)-32)*(5/9)

def f_to_c(c):
    return (1.8*int(c))+32

t=input("What is the value to be converted? ")
q=input("Input c for celsius or f for fahrenheit.")

if(q == 'c'):
    print(f'{t}C ~= {f_to_c(t):.2f}F')
elif (q == 'f'):
    print(f'{t}F ~= {c_to_f(t):.2f}C')
