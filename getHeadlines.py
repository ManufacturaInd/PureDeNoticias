# -*- coding: utf-8 -*-
import requests
import json

page = 0
maxPages = 20
url = "http://api.destakes.com/search/?format=json" + "&page=" + str(page)
response = requests.get(url, timeout=10)
# print response.status_code
noticias = []
while(response.status_code == 200 and page < maxPages):
    data = json.loads(response.content)
    for line in data:
        title = line['title']
        if title not in noticias:
               noticias.append(title)
    page += 1
    # print "estou no pedido nº",page
    url = "http://api.destakes.com/search/?format=json" + "&page=" + str(page)
    response = requests.get(url, timeout=30)
file = open("headlines.txt",'w')
file.write("\n".join(noticias).encode("utf-8"))
file.close()
