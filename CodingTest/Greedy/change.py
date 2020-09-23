n = int(input()) # 금액
count = 0 # 동전 개수를 확인할 변수 선언

# 큰 단위 화폐부터 차례대로 확인
change_list = [500, 100, 50, 10]

for change in change_list:
    count += n // change # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= change

print(count)


