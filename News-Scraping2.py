from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?&where=news&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])


##################################
for article in articles:
    title = article.select_one('dl > dt > a').text # 제목 뽑아내기
    # sp_nws1 > dl > dt > a
    url = article.select_one('dl > dt > a')['href'] # url 뽑아내기

    # 신문사! #sp_nws1 > dl > dd.txt_inline > span._sp_each_source
    new_co = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')

    # 썸네일!
    thumbnail = article.select_one('div > a')['href']

    # print(title, url, new_co) # 여기에 .text 해도 된다
    ws1.append([title, url, new_co, thumbnail]) #리스트 형태로 넣어야 하는 갑다![] 안에
##################################

wb.save(filename='articles2.xlsx')
driver.quit()