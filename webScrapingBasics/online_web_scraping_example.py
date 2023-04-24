from bs4 import BeautifulSoup
import requests

#declare url
url = "https://www.newegg.ca/sony-wh1000xm4b-bluetooth-headset-black/p/0G6-001C-00614?Description=sony%20wxm4&cm_re=sony_wxm4-_-0G6-001C-00614-_-Product"

#search online using requests library using url
#stores as a html document in result
result = requests.get(url)
#to access written contents of result
resultText = result.text

#decrypt using parser
doc = BeautifulSoup(resultText, "html.parser")

#find prices within website
prices = doc.find_all(string="$")
#get parent of $ string
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)