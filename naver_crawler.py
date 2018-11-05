# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:11:57 2018

@author: int_sub05

네이버 정치 뉴스 속보 크롤링
"""
import requests 
from bs4 import BeautifulSoup as bs

temp_url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&listType=title&sid1=100&date=20181105&page={}"
a_url = []
for i in range(1,10):
    if i == 1:
        a_url.append('https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&listType=title&sid1=100&date=20181105')
    else:
        a_url.append(temp_url.format(i))
        
for url in a_url:
    response = requests.get(url)
    html = response.content
    soup = bs(html, 'html.parser')
    for ele in soup.select('#main_content > div.list_body.newsflash_body > ul > li > a'):
        ele_url = ele["href"]
        #print(ele_url)
        
        ele_response = requests.get(ele_url)
        ele_html = ele_response.content
        ele_soup = bs(ele_html, "html.parser")
                       
        #title = ele_soup.select("#articleTitle")[0].text.strip()
        h3 = ele_soup.select_one("#articleTitle")
        title = h3.text.strip()
        #div = ele_soup.select("#articleBodyContents")[0].text.strip()
        div = ele_soup.select_one("#articleBodyContents")
                              
        if div:
            div.script.decompose() #<script type="text/javascript"> ~ </script>
            contents = div.text
            contents = contents.strip()
            contents = div.text.strip()
            
        print("==============================================")
        print(title)
        print(contents)
        print("==============================================")
