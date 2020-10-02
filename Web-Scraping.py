## Web scraping
# 웹 페이지 상에서 원하는 결과를 가지고 오는 것 == web scraping
# 크롤링은 사실,, 구글이나 네이버 같은 검색엔진들이 다니면서 웹페이지들을 가지고 오는 것!
# 거의 둘다 혼용되서 사용된다! 비슷해
# 브라우저를 제어해서, 브라우저에서 받아온 코드를,, 그 안에서 원하는 것을 속아 내는 것!
# 2가지 패키지가 필요하다.
# 브라우저를 제어할 수 있는 것
# 브라우저가 그려주고 있는 것 중에서 원하는 것만 가지고 올 수 있게 해주는 것!

# 셀레니움을 설치해야한다. : 브라우저를 자동 제어 하는 것

# # 셀레니움도 시작코드, 즉 뼈대 코드가 있어서 복사 붙여넣기!
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver')
#
# driver.get("http://www.naver.com")

# 셀레니움으로 자동화하고, 뷰티풀숲으로 속아내고 싶은 거 속아 내고!
# 브라우저는 서버에서 내려준 것을 그대로 그려주기만 한 것!
# 이미 받아왔으니 내가 코드를 변경하면 바꿀 수 있다.
# 받아온 브라우저 코드에서 내가 찾는 것을 찾기란 쉽지 않다, 그래서 bs4로 찾아쓴다

# 크롤링 기본세팅 코드
# dload는 저장
import dload

from bs4 import BeautifulSoup # 뷰티풀숲은 브라우저가 보고 있는 것 중, 원하는 것을 속아 내는 것!
from selenium import webdriver
import time # 파이썬 내장함수! 나중에 필요해

# 드라이버로 해당 파일 로딩해 주세요!
driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
# 페이지가 로딩되는 시간이 있기 때문에, 5초동안 파이썬 쉬어라!
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

# 페이지에서 받아온 것들을 req에 저장해서
req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.

# req를 bs에 넣고! 이제 내가 원하는 부분만 속아 내는 것이여!
soup = BeautifulSoup(req, 'html.parser')

## bs를 사용하는 방법은 크게 2가지만 기억하자
# select와 select_one!

###################################
# '이미지검사 해서 Copy selector로 복사한 부분' 카피셀럭터로 속아낸다!!!!
# 한가지 이미지 src 뽑기
# thumnails = soup.select_one('#imgList > div:nth-child(1) > a > img')['src'] # 해당 코드를 들고온다! [src] 우리는 src값이 필요한데 여기서 볼 수 있다.
# 검색한 이미지들이 "nth-child(1)" 이 부분만 달라

## 여러가지 이미지 src 뽑기
i = 1
thumnails = soup.select('#imgList > div > a > img')
for thumnail in thumnails:
    img = thumnail['src']
    dload.save(img, f'img/{i}.jpg') #이미지를 저장하는데, img 폴더에, 1.jpg 라고 저장할꺼야
    i += 1

###################################
driver.quit() # 끝나면 닫아주기