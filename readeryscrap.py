import requests
from bs4 import BeautifulSoup as b4

url = "https://readery.co/best-sellers"
web_data = requests.get(url)
# print(web_data.text)
soup = b4(web_data.text,'html.parser')
# print(soup)
find_word = soup.find_all("div",{"class":"book-title"})
price = soup.find_all("p",{"class":"price"})
name = []
pricelit = []
for i in find_word:
    print(i.h3.a.get_text(strip=True))


for j in price:
    print(j.span.get_text(strip=True))