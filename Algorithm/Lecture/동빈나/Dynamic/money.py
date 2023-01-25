# 효율적인 화폐 구성
# O(n * m)

# 정답

n, m = map(int, input().split())

# N개의 화폐 입력 받기
array = []
for _ in range(n):
    array.append(int(input()))

# DP 테이블 초기화 (m의 범위: 1 <= m <= 10000)
d = [10001] * (m + 1)

# 바텀업 방식 진행
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        # (i - k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# M원을 만드는 방법이 존재하지 않는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
