# if문

"""
if 조건:
    실행명령문
"""

# # 날씨 예제
# whether = input("오늘 날씨 어때요? ")

# if whether == "비" or whether == "눈": # 조건1과 조건2를 엮을 때 값만 사용하면 안된다. (다 맞다고 인식이 됨)
#     print("우산을 챙기세요.")
# elif whether == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요 없습니다.")

# 기온 예제

temp = int(input("기온은 몇 도인가요? "))
if temp >= 30:
    print("겁나 더우니까 나가지 마세요.")
elif temp < 30 and temp >= 10:
    print("선선한 날씨네요.")
elif 0 <= temp < 10:  
    print("외투를 챙기세요.")
else:
    print("겁나게 추우니까 나가지 마세요.")