# import requests
import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen

from urllib.parse import urljoin

# Get the webpage name from the user
webpage_name = input("Enter the name of the Player: ")

# Construct the URL
base_url = "https://en.wikipedia.org/wiki/"
url = urljoin(base_url, webpage_name)

# # Send the request
# response = requests.get(url)

req= Request(url,headers={'User-Agent':'Mozilla/5.0'}) 

webpage=urlopen(req).read()
mydata=webpage.decode("utf8")
f=open('.\playerName.html','w',encoding="utf-8")
f.write(mydata)
f.close


# # Get the HTML code
# html = response.content

# # # Print the HTML code
# # print(html)

# mydata=response.text
# f=open('webpage_name.html','w',encoding="utf-8")
# f.write(mydata)
# f.close

