# ord() : 문자를 숫자로 변환
# chr() : 숫자를 문자로 변환

# 대문자 변환 함수 선언
def change_upper(upper_alpha):
    return chr(65 + 90 - ord(upper_alpha))   

# 소문자 변환 함수 선언
def change_small(small_alpha):
    return chr(97 + 122 - ord(small_alpha))

# 문자열 리스트로 입력 받기
string = list(input())
result = ""

# 리스트 요소 알파벳 단위로 반복
for alpha in string:
    # 대문자인 경우
    if 65 <= ord(alpha) <= 90:
        result += change_upper(alpha)
    # 소문자인 경우
    elif 97 <= ord(alpha) <= 122:
        result += change_small(alpha)
    # 그 외의 경우 (숫자, 띄어쓰기, 특수문자 등)
    else:
        result += alpha

print(result)