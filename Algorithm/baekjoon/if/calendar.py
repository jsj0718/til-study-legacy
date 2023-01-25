# 윤달인 연도 구하는 문제

"""
4와 400의 배수 - > 1

100 배수 or 나머지 -> 0

즉 우선순위가
400 -> 100 -> 4 -> 나머지 순으로 진행된다.
"""

# 내 답안
# year = int(input())
# if year % 400 == 0:
#     print(1)
# elif year % 100 == 0:
#     print(0)
# elif year % 4 == 0:
#     print(1)
# else:
#     print(0)

# 숏코딩
y=int(input())
# print(+(y%400<1,y%4<1)[y%100>0]) # (result1(False), result2(True))[condition]

print(+(y%400<1, y%4<1)[y%100>0]) # +(result1(False),result2(True))[condition], 위 식에서 맨 앞에 +를 붙이면 True는 1, False는 0으로 계산한다.


