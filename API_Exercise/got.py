import requests
import json


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
    with open(fileName) as f:
        data=json.load(f)
        return data

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




#These are here for when i want to get the data off of the internet again.
# got_url_name()
# got_url_houses()

characters=read_file(charfileName)
houses=read_file(housefileName)

for c in characters:
    houseList=c["allegiances"]
    allegences=getCharHouses(houseList,houses)
    print(f'name:{c["name"]} homes: {allegences}')
