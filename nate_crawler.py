# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:56:44 2018

@author: int_sub05

네이트 정치 뉴스 속보 크롤링
"""
import requests 
from bs4 import BeautifulSoup as bs

temp_url = "https://news.nate.com/recent?cate=pol&mid=n0201&type=t&date=20181105&page=={}"
a_url = []
for i in range(1,10):
    if i == 1:
        a_url.append('https://news.nate.com/recent?cate=pol&mid=n0201&type=t&date=20181105')
    else:
        a_url.append(temp_url.format(i))
        
for url in a_url:
    response = requests.get(url)
    html = response.content
    soup = bs(html, 'html.parser')
    for ele in soup.select('#newsContents > div.postListType.noListTitle > div.postSubject > ul > li > a'):
        ele_url = "https://news.nate.com" + ele["href"]
        #print(ele_url)
        
        ele_response = requests.get(ele_url)
        ele_html = ele_response.content
        ele_soup = bs(ele_html, "html.parser")
                       
        title = ele_soup.select("#articleView > h3")[0].text.strip()
        contents = ele_soup.select("#realArtcContents")[0].text.strip()
        print("==============================================")
        print(title)
        print(contents)
        print("==============================================")