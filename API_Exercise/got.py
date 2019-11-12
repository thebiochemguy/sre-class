import json
import requests
import sys


charfileName="char_got.json"
housefileName="houses_got.json"

def got_url_name():
    last_page=44
    pageSize=50

    data=[]
    for page in range(1,last_page):
        url=f'https://www.anapioficeandfire.com/api/characters?page={page}&pageSize={pageSize}'
        response=requests.get(url)
        results=response.json()
        for result in results:
            data.append(result)

        
    with open(charfileName, 'w',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_file(fileName):
    try:
        with open(fileName) as f:
            data=json.load(f)
            return data
    except FileNotFoundError:
        print("\nLooks like the files dont exist in this directory please run from directory where json files are located.\n")
        sys.exit()

def got_url_houses():
    last_page=10
    pageSize=50

    data=[]
    for page in range(1,last_page):
        url=f'https://www.anapioficeandfire.com/api/houses?page={page}&pageSize={pageSize}'
        response=requests.get(url)
        results=response.json()
        for result in results:
            data.append(result)

        
    with open(housefileName, 'w',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def getCharHouses(homeurls,houses):
    data=[]
    for home in homeurls:
        #Need to remove one to take into account that arrays start at 0
        id=int(home.split("/")[-1]) - 1 
        data.append(houses[id]["name"])

    return data

def printCharacterList():
    for c in characters:
        houseList=c["allegiances"]
        allegences=getCharHouses(houseList,houses)
        print(f'{c["name"]} {allegences}')


def printHouseInfo(name):
    print(f'looking for {name}')
    for c in characters:
        if (c["name"].lower() == name.lower()):
            houseList=c["allegiances"]
            for home in houseList:
                print("\n")
                id=int(home.split("/")[-1])-1
                for key in houses[id]:
                    print(f'{key}: {houses[id][key]}')
                _=input("\nPress enter to continue")
            

#Uncomment the two lines below, to get the info off the internet.
#got_url_name()
#got_url_houses()

#Reading files to prevent constant api calls... 
#Make sure you run the program from the same directory where the char_got.json and houses_got.json are located.
characters=read_file(charfileName)
houses=read_file(housefileName)

choice=""
while choice.lower() != "exit":
    printCharacterList()
    choice=input("\nPlease input a character name or \"exit\" to exit: ")
    printHouseInfo(choice)