phonebook={
    "Igor": "857-485-2935",
    "Melissa": "123-456-7890",
    "Jazz": "789-0984-9873",
    }

def menu_print():
    print("Electronic Phone Book")
    print("="*10)
    print("1. Look up entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entry")
    print("5. Quit")
    x=int(input("What do you want to do (1-5)"))
    if(x<1 or x > 5 ):
        print("Im out")
        quit()
    else:
        return x

def add_entry():
        name=input("What is the new name? ")
        name.strip().lower()
        num=input("What is the phone number? ")
        phonebook[name]=num

def list_entries():
    name=input("Who are you looking for? ")
    name.strip().lower()
    num=phonebook.get(name,"Name not found")
    print(num)

def del_entry():
    names=phonebook.keys()
    for n in names:
        print(n)
    name=input("Delete who? ")
    name.strip().lower()
    if(phonebook.get(name).lower() != None):
        del phonebook[name]
    else:
        print("Entry does not exist: ")


while True:
    selection=menu_print()
    if(selection==5):
        quit()
    elif(selection==4):
        print(phonebook)
    elif(selection==3):
        del_entry()
    elif(selection==2):
        add_entry()
    elif(selection==1):
        list_entries()