# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

a = list(map(int, input().split()))
n = len(a)

def sum_n(a):
    n = len(a)
    sum_a = 0
    for i in range(n):
        sum_a += a[i]
    return sum_a

print(sum_n(a))
    

