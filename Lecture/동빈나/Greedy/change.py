# 거스름돈 최소 개수
# 거스름돈이 그리디로 가능한 이유는 500, 100, 50, 10이 항상 작은 단위의 배수이기 때문이다.

money = int(input())
change_list = [500, 100, 50, 10]
cnt = 0

for change in change_list:
    cnt += money // change
    money %= change

print(cnt)