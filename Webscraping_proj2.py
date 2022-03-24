from lib2to3.pytree import convert
from bs4 import BeautifulSoup, Comment
import requests
import regex as re
import xml
from selenium import webdriver
import time
import random
from jason_algorithm import Tranformtojson

random.seed(time.time())
def web_scrap(url):
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # executable_path param is not needed if you updated PATH
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")
    #browser.quit()
    return soup

def get_all_link_and_next_page(url):
    # main_content = soup.find("div",{"class": "clearfix"}).find("section",{"class" : "primary"})
    website = url
    soup = web_scrap(website)
    all_div = soup.find_all("h1",{"class":"entry-title post-title"})
    news_link = [link_.findChild("a")['href'] for link_ in all_div]
    nextpage = soup.find("a",{"class": "next page-numbers"})
    nextpage = nextpage['href']
    return [news_link,nextpage]
    #array 0 = [news_link]
    #array 1 = next_page
def get_header_and_context(url):
    so = web_scrap(url)
    data = so.find("section",{"class" : "primary"}).find("article")
    head = data.find("h1",{"class":"entry-title post-title"})
    context = data.find("div",{"class":"entry clearfix"}).find_all("p")
    get_header = head.get_text()
    # get_context = context.get_text()
    regexp = re.compile(r'\n', re.UNICODE)
    text_header = regexp.sub('', get_header)
    # text_context = regexp.sub('', get_context)
    text_context = ""
    for i in context:
        #  print(i.get_text())
        text_context += i.get_text()
    return [str(text_header),text_context.replace(u'\xa0', u' ')]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\Keroro\Desktop\Learn-Python\chromedriver')
start_website = "https://www.compgamer.com/mainpage/author/cgnadmin/page/23"
# browser.get(start_website)
# time.sleep(3)
# html = browser.page_source
# soup = BeautifulSoup(html, features="html.parser")
next_page = start_website
all_link = []
count = 0
# start = 0
# end = 1000

while(True):
    #print(before_page,next_page)
   
    # time.sleep(3)
    # if count == 5:
    #     break
    # link = get_all_link_and_next_page(soup)
    # all_link.append(link)
    # count += 1
    # start = end
    # end +=1000 
    link = get_all_link_and_next_page(next_page)
    all_link += link[0]
    if count == 10:
        break
    before_page = next_page
    next_page = link[1]
    count += 1
    
    #time.sleep(random.uniform(10.0,1000.0)/1000)
print(all_link)

f = open("all_link.txt", 'w')
with open("all_link.txt", 'w',encoding='utf-8') as f:
    for link in all_link:
        f.write(link+",")

text_all_link = open("all_link.txt", "r")
lines = text_all_link.read()
all_text_link = lines.split(",")
all_text_link.pop()
len(all_text_link)

for index,link in enumerate(all_text_link):
    text = get_header_and_context(link)
    print(text)
    convert = Tranformtojson(index+213,"Mr.O",text[0],text[1])
    convert.tranform()
    # filename = 'codeman'+str(index+762)+'.txt'
    # # f = open('AkumaFaster'+filename, 'w')
    # with open('codeman\\'+filename, 'w',encoding='utf-8') as f:
    #     f.write(text[0])
    #     f.write("\n\n")
    #     f.write(text[1])
    
browser.quit()