import requests
import json


fileName="got.json"

def got_url():
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

        
    with open(fileName, 'a',encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_file():
    with open(fileName) as f:
        data=json.load(f)
        return data


i=0
    
read_file()
for c in read_file():
     for x in c:
         # print(c[4]["name"])
        i+=1
        print(f'id:{i} name:{x["name"]}')
