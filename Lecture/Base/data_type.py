# --- 자료형 ---

# 1) 숫자형(int, float)

print(5) # int
print(-10) # int
print(3.14) # float
print(5+10) # -도 동일
print(2*8) # /도 동일
print(3*(3+1)) # ()로 우선순위 변경 가능

# 2) 문자형(string)

print('풍선')
print('ㅋㅋㅋㅋㅋㅋ')
print('ㅋㅋㅋ' '야호') # '' 와 '' 사이가 빈 공간이면 띄어쓰기가 안됨
print('ㅋㅋㅋ' + '야호') # ''와 '' 사이에 , 있으면 띄어쓰기가 됨
print('ㅋ' * 9) # * int로 문자열 반복

sentense1 = "나는 소년입니다."
print(sentense1)

sentense2 = "파이썬은 쉬워요"
print(sentense2)

sentense3 = """
나는 소년이고요,
파이썬은 쉬워요.
"""
print(sentense3) # """와 """ 사이의 줄바꿈이 포함되어 총 4줄이 출력된다.

sentense4 = """\
나는 소년이고요,
파이썬은 쉬워요.\
"""
print(sentense4) # """와 """ 사이의 처음과 끝에 \를 추가하면 줄바꿈이 없어진다.

# 3) boolean (True or False)

print(5 > 10) # True
print(5 < 10) # False
print(True)
print(False)
print(not True) # False
print(not False) # True
print(not(5 > 10)) # True

# --- 문자열 포맷 ---

print("a" + "b") # ab
print("a" "b") # ab
print("a", "b") # a b

# 방법 1 (%)
print("나는 %d살 입니다." % 20) # %d는 정수값만 가능
print("나는 %s를 좋아해요." % "python") # %s는 문자열 (전부 가능)
print("Apple은 %c로 시작해요." % "A") # %c는 character로 한 글자만 가능

print("나는 %s살 입니다." % 20) # %s는 전부 문자열로 바꿔 대입이 가능해서 만능
print("나는 %s색과 %s색을 좋아해요." % ("빨간", "파란"))

# 방법 2 ({}.format)
print("나는 {0}살입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요.".format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "Red"))

# 방법 4
age = 26
color = "Black"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # ssafy Algorithm 문제 첫 부분에 해당

# --- 탈출 문자 ---

# \n : 줄바꿈
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

# \', \"" : 문장 내에서 따옴표
# 저는 "정세진" 입니다.
print("저는 '정세진'입니다.")
print('저는 "정세진"입니다.')
print("저는 \'정세진\'입니다.")
print("저는 \"정세진\"입니다.")

# \\ : 문장 내에서 \
# print("C:\Users\user\Desktop\PythonWorkspace") # \~ : 탈출 문자 형식인데, 정해진 코드가 아니기 때문에 오류가 남.
print("C:\\Users\\user\\Desktop\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # 커서를 맨 앞으로 이동 후 Pine을 맨 앞부터 4칸까지 대체

# \b : 백스페이스
print("Redd\bApple") # 백스페이스로 d 하나를 삭제

# \t : 탭
print("Red\tApple")