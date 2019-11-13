from bs4 import *
import requests as req
import os

webreq = req.get("https://www.pexels.com/@hiteshchoudhary" )
Soup = BeautifulSoup(webreq.text, "html.parser")

links = []
img_link = Soup.select('img[src^= "https://images.pexels.com/photos"]')
for img in img_link:
    links.append(img['src'])

os.mkdir("web_crawler_result")

for index, img_link in enumerate(links):
    img_data = req.get(img_link).content
    with open("web_crawler_result\\" + str(index+1) + ".jpg", 'wb+') as f:
        f.write(img_data)
        f.close()