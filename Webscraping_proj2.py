from bs4 import BeautifulSoup, Comment
import requests
import regex as re
import xml
from selenium import webdriver
import time
import random

random.seed(time.time())
# def web_scrap(url):
#     # options = webdriver.ChromeOptions()
#     # options.add_argument('--headless')
#     # executable_path param is not needed if you updated PATH
#     browser.get(url)
#     time.sleep(3)
#     html = browser.page_source
#     soup = BeautifulSoup(html, features="html.parser")
#     #browser.quit()
#     return soup

def get_all_link_and_next_page(soup):
    # main_content = soup.find("div",{"class": "clearfix"}).find("section",{"class" : "primary"})
    all_div = soup.find_all("h1",{"class":"entry-title post-title"})
    news_link = [link_.findChild("a")['href'] for link_ in all_div]
    # nextpage = soup.find("div",{"class": "page-nav td-pb-padding-side"}).find_all("a")
    # nextpage = nextpage[-1]['href']
    return news_link
    #array 0 = [news_link]
    #array 1 = next_page
# def get_header_and_context(url):
#     so = web_scrap(url)
#     data = so.find("div",{"class" : "td-pb-span8 td-main-content"}).find("div",{"class":"td-ss-main-content"}).find("article")
#     head = data.find("div",{"class":"td-post-header"}).find("header",{"class":"td-post-title"}).find("h1",{"class":"entry-title"})
#     context = data.find("div",{"class":"td-post-content"}).find("div",{"itemprop": "articleBody"})
#     get_header = head.get_text()
#     get_context = context.get_text()
#     regexp = re.compile(r'\n', re.UNICODE)
#     text_header = regexp.sub('', get_header)
#     text_context = regexp.sub('', get_context)
#     return [str(text_header),str(text_context)]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\Keroro\Desktop\Learn-Python\chromedriver')
start_website = "https://www.compgamer.com/mainpage/author/viruss"
browser.get(start_website)
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, features="html.parser")
# prevois_height = browser.execute_script("return document.body.scrollHeight")
all_link = []
count = 0
# start = 0
# end = 1000

while(True):
    #print(before_page,next_page)
   
    # time.sleep(3)
    if count == 5:
        break
    link = get_all_link_and_next_page(soup)
    all_link.append(link)
    count += 1
    # start = end
    # end +=1000 

    
    #time.sleep(random.uniform(10.0,1000.0)/1000)
print(all_link)