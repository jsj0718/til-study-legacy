# 데이터의 개수 N과 데이터 입력받기
n = int(input())
data = list(map(int, input().split()))

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]

for i in range(n):
    sum_value += data[i]
    prefix_sum.append(sum_value)

# 구간 합 계산 (세 번째 수부터 네 번째 수까지의 합, 30 + 40)
left, right = map(int, input().split())

print(prefix_sum)
print(prefix_sum[right] - prefix_sum[left - 1])