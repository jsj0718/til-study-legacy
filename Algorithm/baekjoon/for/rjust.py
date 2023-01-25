# 오른쪽 정렬 문제 (별 찍기)

n = int(input())

for i in range(n):
    print(("*" * (i+1)).rjust(n)) # rjust로 오른족 정렬
