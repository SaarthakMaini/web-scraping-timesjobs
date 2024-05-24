from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
tags = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
for tag in tags:
    print(f"Company Name : {tag.h3.text.strip()}\nLocation: {tag.span.text}\nLink: {tag.a['href']}\n".replace(' ',''))
