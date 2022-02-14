import requests
from bs4 import BeautifulSoup

headers = {'Accept': "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
           'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
url = 'https://hh.ru/'
req = requests.get(url, headers=headers)
src = req.text
# print(src)

# with open("index.html", 'w') as file:
# file.write(src)
with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.findAll(class_="bloko-gap bloko-gap_top")
for item in all_products_hrefs:
    print(item)
