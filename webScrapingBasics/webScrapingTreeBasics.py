from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
result =  requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

#get tbody tag which holds all the crypto currency
tbody = doc.tbody
#access children of tbody parent
trs = tbody.contents

#loop through table rows
prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    #name is stored in ptag
    fixed_name = name.p.string
    #price is stored in atag
    fixed_price = price.a.string
    #store in dictionary
    prices[fixed_name] = fixed_price

print(prices)
