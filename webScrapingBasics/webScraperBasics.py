#import webscraping library
from bs4 import BeautifulSoup;

#read html document
with open("index.html","r") as f:
    doc = BeautifulSoup(f, "html.parser")

#this holds the full html file
print(doc)
#you can use doc.prettify() to clean up the indentation

#to pull the title
tag = doc.title
print(tag)

#to access only the string inside of tag
print(tag.string)
#able to alter inside html doc
tag.string = "hello"
print(doc)

#to find specific tag
tags = doc.find_all("a")

#to find all occurances of tag
print(tags)

#find all puts it into array of string
print(tags[0])




