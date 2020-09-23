# while 문

# 예제 1
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님, 주문하신 커피 나왔습니다. 폐기까지 {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기되었습니다.")

# 예제 2
# customer = "아이언맨"
# index = 1
# while True: # 무한 루프, ctrl + c로 강제 종료
#     print("{0}님, 커피 나왔습니다. {1}회 호출".format(customer, index))
#     index += 1

# 예제 3
customer = "정대만"
person = "unknown"

while person != "정대만":
    print("{0}님, 커피 나왔습니다.".format(customer))
    person = input("성함이 어떻게 되세요? ")
    