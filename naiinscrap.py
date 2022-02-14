import requests
from bs4 import BeautifulSoup as b4

url = "https://www.naiin.com/category?type_book=best_seller&product_type_id=1"
web_data = requests.get(url)
# print(web_data.text)
soup = b4(web_data.text,'html.parser')
# print(soup)
find_word = soup.find_all("a",{"class":"itemname"})
price = soup.find_all("p",{"class":"txt-price"})
name = []
for i in range(0,80):
        # print(i.get_text(strip=True))
        print(find_word[i].get_text(strip=True),price[i].get_text(strip=True))
