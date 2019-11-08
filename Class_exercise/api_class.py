# import urllib.parse
#* import requests
import json
# x='{"name":"John","age":30,"city":"New York"}'
# y=json.loads(x)
# print(y["age"])
# original="<New York>"
# encodedString=urllib.parse.quote_plus(original)
# print(f'{encodedString}')
# print(y[0]['title'])

# import requests

# response=requests.get('http://jsonplaceholder.typicode.com/comments')

# x=0
# for item in response.json():
#     x+=1
#     print(f'{x} Name: {item["name"]} \tEmail {item["email"]}'.expandtabs(100))


# import requests

# new_post={'userId':10, 'title':'a title', 'body':'something something'}

# response=requests.post('http://jsonplaceholder.typicode.com/posts', json=new_post)

# print(response)

# x=0
# for item in response.json():
#     x+=1
#     print(f'{x} Name: {item["name"]} \tEmail {item["email"]}'.expandtabs(100))

import requests


#url=f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=5c65aa69e2b51360cba1f2889e48d203'


# sym="XOM"
# intvl="5min"
# apikey="XA49N0XBTATREBLI"
# url=f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={sym}&interval={intvl}&apikey={apikey}'
# # url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=XOM&interval=5min&apikey=XA49N0XBTATREBLI"

import requests
#import logging

#logging.basicConfig(level=logging.DEBUG)
__apikey__="229da24e9dc943e05c11b7d59bbf653e"
units="imperial"
while True:

    
    city=input("Please enter the name of a city: ")
    
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&APPID={__apikey__}'

    response=requests.get(url)
    results=response.json()


    print(f'Current temp: {results["main"]["temp"]}')

