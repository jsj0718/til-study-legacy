"""
url을 통해 접속하면 웹 브라우저에서 코드를 분석하고 처리해서 클라이언트 화면에 나타낸다.
"""

import requests

target = "https://www.google.com"
# 특정 url에 get 방식으로 접근해서 html 문서를 받아온다.
response = requests.get(url=target)
# 응답으로부터 텍스트 값(코드)을 출력
print(response.text)