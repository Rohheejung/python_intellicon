# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:01:45 2018

네이버 뉴스 기사 웹 크롤러 모듈
"""

from bs4 import BeautifulSoup
import urllib.request

# 출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'
# 긁어 올 URL
URL = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=022&aid=0003314670'

# 크롤링 함수
def get_text(URL):
    source_code_from_URL=urllib.request.urlopen(URL)
    soup=BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text=''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text

# 메인 함수
def main():
    open_output_file=open(OUTPUT_FILE_NAME, 'w')
    result_text=get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()
    
if __name__=='__main__':
    main()

