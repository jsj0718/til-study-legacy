# --- 문자열 처리 함수 ---
python = "Python is Amazing"

print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # True, python 변수의 0번째 인덱스인 P가 upper인지 확인하는 함수(is~()는 True or False를 확인)

print(len(python)) # 17, 길이(띄어쓰기 포함)를 나타내는 함수

print(python.replace("Python", "Java")) # python의 내용 중 old 부분을 new 부분으로 교체

index = python.index("n") # n이 몇번째 인덱스인지 확인하는 함수
print(index) # 5
print(python.index("n", index+1)) # 15, 5번째 인덱스 값인 n 이후의 n을 탐색, 15번째 인덱스 값인 n을 찾음
# print(python.index("Java")) # index 함수는 찾는 값이 없으면 오류를 발생시킴.

# find도 index와 유사
print(python.find("n")) # 5, 왼쪽부터 탐색
print(python.rfind("n")) # 15, 오른쪽부터 탐색
print(python.find("Java")) # -1, find는 찾는 값이 없으면 -1을 출력

print(python.count("n")) # 2, python 내 "n"이 몇 개인지 카운트 해주는 함수

# --- 숫자 처리 함수 ---
print(abs(-5)) # 5, 절대값
print(pow(4, 2)) # 4^2 = 16, pow(a,b) = a^b, 제곱
print(max(1,4,2,5)) # 5, 최대값 -> 함수 내제 내용 찾아보기
print(min(1,4,2,5)) # 1, 최솟값 -> 함수 내제 내용 찾아보기
print(round(3.14)) # 3, 반올림
print(round(4.99)) # 5, 반올림

from math import *
print(floor(4.99)) # 4, 버림
print(ceil(4.01)) # 5, 올림
print(sqrt(16)) # 4, 제곱근(float 형태)


# --- 랜덤 함수 ---
from random import *

print(random()) # 0.0부터 1.0 미만까지 임의의 숫자 출력
print(random()*10) # 0.0부터 10.0 미만까지 임의의 숫자 출력
print(int(random()*10)) # 0부터 10 미만까지 임의의 숫자 출력

# 로또 번호 출력 (중복될 가능성 존재)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

# 더 쉽게 표현하는 방법(randrange와 randint 이용)
print(randrange(1,46)) # 1부터 46미만의 임의의 숫자를 출력
print(randint(1,45)) # 1부터 45 이하의 숫자를 출력

