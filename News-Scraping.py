from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# articles = soup.select_one('#sp_nws1 > dl > dt > a') # 내가 원하는 기사 제목의 html 코드 정보
# print(articles.text) # html 정보 중에서 text만 들고오겠다
# # 문제는 기사들을 가져오려고 해도,, 규칙이 달라! sp_nws1 이부분이 다른데, 규칙이 있는 것이 아니다
# # 그래서,, 그 윗단! li 윗단의 ul 윗단의 div에서! li를 들고 오겠다! 라고 해야돼

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li') # > li를 붙여준 것!
# select_one하면 html 코드 형태로 나오고, select 하면 list 형태로 나온다
for article in articles:
    title = article.select_one('dl > dt > a').text # 제목 뽑아내기
    url = article.select_one('dl > dt > a')['href'] # url 뽑아내기

    # 신문사! #sp_nws1 > dl > dd.txt_inline > span._sp_each_source
    new_co = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사', '')


    print(title, url, new_co) # 여기에 .text 해도 된다
    # 웹스크레핑은 이렇게 해야한다! 라는 정해진 것이 없다. 왜냐면 웹 사이트 마다 html이 다 다르고
    # 원하는 정보들이 딱 배운대로 적혀있을 가능성이 적다! 그래서 이래 저래 접근해서
    # 원하는 정보를 찾아내는 게 딱 좋다!

# 긁어온 정보들을 엑셀에 저장하려면!!
# openpyxl 이라는 아주 훌륭한 패키지가 있다!

#####################

driver.quit()