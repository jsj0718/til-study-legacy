n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환 (오름차순)
array.reverse()

# 1차원 DP 테이블 초기화
d = [1] * n

# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)

# 열외해야 하는 병사의 최소 수 출력
print(n- max(d))