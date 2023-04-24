from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
#access tags and values like dictionary
tag['value'] = 'new value'

#print attributes
print(tag.attrs)

#find all tags that contain "p, div" or "li
tag = doc.find_all(["p", "div", "li"])
print(tag)

#find tag with specific text
tags = doc.find_all(["option"], string="Undergraduate")

#find differnet class names
tags = doc.find_all(class_="btn-item")

#use regular expressions
#use re.compile
tags = doc.find_all(string=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())


#add limit to search query
tags = doc.find_all(string=re.compile("\$.*"), limit=1)
for tag in tags:
    print(tag.strip())

#changing content within html doc
tags = doc.find_all("input",type="text")
for tag in tags:
    tag['placeholder'] = "I changed you"

with open("changed.html", "w") as file:
    file.write(str(doc))