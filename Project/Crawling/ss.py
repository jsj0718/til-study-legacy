# # python에서 HTTP 요청을 보내는 모듈
# import requests
# # bs4 라 불리는 html 분석 라이브러리
# from bs4 import BeautifulSoup

# # 유저 설정
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# # 네이버 메인이 아닌 DataLab 페이지
# url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

# # User 설정
# res = requests.get(url, headers = headers)

# # res.content 주의
# soup = BeautifulSoup(res.content, 'html.parser')

# # span.keyword 정보를 선택
# data = soup.select('span.keyword')

# # for 문으로 출력해준다.
# for item in data:
#     print(item.get_text())


# JSON 파일을 받아 Data를 뽑아내는 방식

import requests 
json = requests.get("https://www.naver.com/srchrank?frm=main").json() 
ranks = json.get("data") 

f = open("memo.txt", "w", encoding="UTF-8")
for r in ranks: 
    rank = r.get("rank")
    keyword = r.get("keyword") 
    data = "{0}위 : {1}".format(rank, keyword) + "\n"
    f.write(data)
f.close()