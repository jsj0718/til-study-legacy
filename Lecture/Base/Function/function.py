# 함수

# def 함수이름(매개변수1, 매개변수2, ...):
#    내용
#    return # 출력값

# 계좌 생성 (입력값, 출력값 X)
def open_account(): # 입력값 X
    print("새로운 계좌가 개설되었습니다.") # 출력값 X

# open_account() # return값이 없기 때문에 print()를 활용할 수 없다.

# 입금 (입력값, 출력값 O)
def deposit(balance, money): # 입력값
    print("{0}원이 입금되었습니다. 현재 잔액은 {1}원 입니다.".format(money, balance + money))
    return balance + money # 출력값

# 출금 (입력값, 출력값 O)
def withdraw(balance, money):
    print("{0}원이 출금되었습니다. 현재 잔액은 {1}원 입니다.".format(money, balance - money))
    if balance < money:
        print("출금하는데 실패했습니다. 현재 잔액은 {0}원입니다.".format(balance))
        return balance
    return balance - money

def withdraw_night(balance, money):
    commission = 200
    return commission, balance - money - commission

# def withdraw_night(balance, money):
#     commission = 200
#     if balance < money + commission:
#         print("출금에 실패했습니다.")
#         return commission, balance
#     print("수수료는 {0}원입니다. 현재 {1}원 출금되어 남은 잔액은 {2}원입니다.".format(commission, money, balance - money - commission))
#     return commission, balance - money - commission



# 입금 예시
balance = 0
balance = deposit(balance, 1000)
print(balance)

# 출금 예시
balance = withdraw(balance, 500)
print(balance)

# 출금(수수료 포함) 예시 1
commission, balance = withdraw_night(balance, 300) # commission이 함수 내 commission과 같은 값이 되어 적용됨. (balance도 동일)
print("수수료는 {0}원입니다. 현재 잔액은 {1}원입니다.".format(commission, balance))

# 출금(수수료 포함) 예시 2
# commission, balance = withdraw_night(balance, 310)
# print(withdraw_night)