import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver') # driver로 chromedriver 파일 로딩
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%ED%98%84%EB%B9%88")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

i = 1
thumnails = soup.select('#imgList > div > a > img')
for thum in thumnails:
    img = thum['src']
    dload.save(img, f'img2/{i}.jpg') #앞에 img는 받는 변수고, 뒤에 저장할 폴더가 들어감
    i += 1

driver.quit()