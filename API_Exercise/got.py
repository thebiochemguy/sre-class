import requests
import json


charfileName="char_got.json"
housefileName="houses_got.json"

def got_url_name():
    # i=0
    page=1
    last_page=43
    pageSize=50

    data=[]
    for page in range(0,last_page):
        url=f'https://www.anapioficeandfire.com/api/characters?page={page}&pageSize={pageSize}'
        response=requests.get(url)
        results=response.json()
        data.append(results)

        
    with open(charfileName, 'w',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_file(fileName):
    with open(fileName) as f:
        data=json.load(f)
        return data

def got_url_houses():
    page=1
    last_page=9
    pageSize=50

    data=[]
    for page in range(0,last_page):
        url=f'https://www.anapioficeandfire.com/api/houses?page={page}&pageSize={pageSize}'
        response=requests.get(url)
        results=response.json()
        data.append(results)

        
    with open(housefileName, 'w',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def getCharHouses(homeurls,houses):
    data=[]
    for home in homeurls:
        for house in houses:
            for h in house:
                if (h["url"] == home):
                    data.append(h["name"])
    return data


#    https://anapioficeandfire.com/api/houses/378

# got_url_name()
# got_url_houses()

i=0
    
characters=read_file(charfileName)
houses=read_file(housefileName)

for c in characters:
     for x in c:
        i+=1
        houseList=x["allegiances"]
        allegences=getCharHouses(houseList,houses)
        print(f'name:{x["name"]} homes: {allegences}')
