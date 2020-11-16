# 돈 입력 받기
money = int(input())

# 돈 리스트 정의
money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]

# 돈의 개수 리스트 정의
money_count = []

# 잔돈 정의
for change in money_list:
    # 돈의 개수 정의
    result = 0
    # 입력 받은 돈을 잔돈으로 나눴을 때 0보다 큰 경우
    if money // change > 0:
        result += money // change
        money = money % change
        money_count.append(result)
    # 그 외의 경우    
    else:
        money_count.append(result)

print(money_count)