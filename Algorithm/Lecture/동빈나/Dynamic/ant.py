# 개미 전사

n = int(input())
array = list(map(int, input().split()))

# 각 순간에 최대값을 저장하는 DP 테이블 선언
d = [0] * n
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    # i-2번째까지의 최대값 + array의 i번째 값 vs i-1번째까지의 최대값을 비교
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d)
