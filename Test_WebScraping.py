from atexit import register
import requests
from bs4 import BeautifulSoup as b4

url = "https://www.ebay.com/itm/265287549827?epid=11051301031&_trkparms=ispr%3D1&hash=item3dc45ec383:g:cTkAAOSwdRdhKTCD&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsStdebXPz4ZTXCT8FI9kPBhwefDFfmEJPNZyN7JX5OlTFDgH5VPiJAveEbXRwtZjJZno1jzEXxNhiOdZ%252FaJbHLqHjixkHIFyXy%252BuajgXazfNL2Pja5hfe4x1u89b8RssuF%252BNCMWzbDS4vauLiCfOg2%252FrrEGlOCdjvkEGN7rVgSLAJRsOQq1VQ08Ffm16s7UXK6MfR2bId%252Fk9qEWnqog%252BU2eHZzfWyA%252FyjyQ1CmHkpauqUBWmeRePQI3NSvU4%252BjXs9GY0v%252BdMaEph9q8rQM5xA%252F9aQssJEdVO%252F%252FSC7oxPZMoHfe20nMyq3bK4%252FJOdnf2MNai0EP6RdPe5%252Fuk7q2dfA6VG8GKYiwOIx72I6GlfkX%252BPn7IThpjFxD7cfxSmbs3wIJjduOaqu0G7A578%252BR7CebjAa0p1BUzPlaAHVRdf9%252BvG2q3VAWxUYyKhovzSzDrS8gDffXwGje31F9Y2nujxmkWC1cau%252FsQEjJVx70rOW%252B2o3Pm0Q5Qq%252Bo49qyGOJcMe3IP%252BbrbXnRxRrZRzTAVjYVT2r%252Fi9oRVhM6fOODS7Rqje45QDrZ9RWYwfk3tAzUxXPRmB4IdAxTTHiMK7V%252BGaUmxqNsSPHd4wlACfJmBWSsSpGSmfVUWsgSFVcXJJmGA7NwqsWzFqOHijB1mGpwjg%252F%252BUyFZgkOwEYZTVUeMJeooS87PgaL45EacbdX%252FgGK6z1nFOsadwvt06kwe%252BHkKjZ0yycM3ASvpnXsNoDNsj6J96sRyyWrDnyiGaCOhSIQxIv5jj80ACR9avY6mAGNXdtJ7rJYSfpjp0WBN5CP%252FhKu3ewCzbUPM4kcFx9w1IyY9uR%252BF%7Cclp%3A2334524%7Ctkp%3ABFBMsNKjk99f"
url2 = "https://www.ebay.com/itm/185281932182?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D20200818143230%26meid%3D876a398ee27a4e7a9750711107d33074%26pid%3D101224%26rk%3D3%26rkt%3D5%26sd%3D265287549827%26itm%3D185281932182%26pmt%3D0%26noa%3D1%26pg%3D2047675%26algv%3DDefaultOrganicWeb%26brand%3DASUS&_trksid=p2047675.c101224.m-1"
url3 = "https://www.ebay.com/itm/294018679165?_trkparms=pageci%3Aad6bee17-8e67-11ec-80fd-f6af9a1ce477%7Cparentrq%3Afdaf8fd217e0a744852fc889fffa2cba%7Ciid%3A1"
web_data = requests.get(url)
# print(web_data.text)
soup = b4(web_data.text,'html.parser')
# print(soup)
find_word = soup.find_all('span',{'class':'u-dspn'})
price = soup.find_all("div",{'class':'mainPrice'})[0]
# print(find_word[0].get_text(strip=True))
regis = b4(price.text,'html.parser')
m = 0
lit = ''
for i in regis:
   lit += i
lit = lit.split('\n')
# print(lit)
realprice = lit[8].replace('Approximately ','').replace('(including shipping)','')
print(find_word[0].get_text(strip=True),realprice)
