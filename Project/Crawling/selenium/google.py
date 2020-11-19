# https://wikidocs.net/61209 참고

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import time

# 검색 키워드 및 다운받을 사진 수량 입력
keyword = input()
count = int(input())

# 크롬 드라이버 가져오기
driver = webdriver.Chrome()
# 구글 이미지 검색창으로 이동
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
# 구글 검색창 요소를 변수에 담기
elem = driver.find_element_by_name("q")
# 키워드 입력 및 검색
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

# 스크롤 최대로 내리기

# 스크롤 내린 후 대기 시간
SCROLL_PAUSE_TIME = 1

# 스크롤 높이 가져오기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 진행
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 페이지 로드 대기 시간
    time.sleep(SCROLL_PAUSE_TIME)

    # 새로운 스크롤 높이를 구한 후 마지막 스크롤 높이와 비교
    new_height = driver.execute_script("return document.body.scrollHeight")
    # 만약 같다면 (변화가 없다면)
    if new_height == last_height:
        try:
            # 결과 더보기를 클릭한다
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            # 그 외에는 break
            break
    last_height = new_height

# 이미지 모든 요소를 변수에 담기
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

# 폴더 생성 (키워드로 된 폴더가 없을 시)
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))

# 이미지 하나씩 호출
for index, image in enumerate(images):
    try:
        image.click()
        time.sleep(2)
        ImgURL = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")

        urllib.request.urlretrieve(ImgURL, "./{}/{}{}.jpg".format(keyword, keyword, (index + 1)))        
        if index + 1 >= count:
            break

    except:
        pass

driver.close()

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# os.walk('절대경로').next()[0] ==> 디렉토리 경로
# os.walk('절대경로').next()[1] ==> 디렉토리 내의 디렉토리 개수
# os.walk('절대경로').next()[2] ==> 디렉토리 내의 파일 개수