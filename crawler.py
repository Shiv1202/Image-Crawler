from bs4 import *
import requests as req
import os

User_id = input()
print(User_id)
webreq = req.get("https://www.pexels.com/@hiteshchoudhary" )
Soup = BeautifulSoup(webreq.text, "html.parser")

links = []
img_link = Soup.select('img[src^= "https://images.pexels.com/photos"]')
for img in img_link:
    links.append(img['src'])
print(links)