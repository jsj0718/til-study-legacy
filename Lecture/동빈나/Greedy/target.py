# n이 1이 될 때까지 반복하는 알고리즘
# O(log N)인 방법

n, k = map(int, input().split())
result = 0

while True:
    # n이 k로 나눠질 수 있는 가장 가까운 수 target을 선언
    target = (n // k) * k
    # n에서 target까지 되는데 필요한 -1 반복과정을 result에 더하기
    result += n - target
    n = target
    
    # 만약 n이 k보다 작은 경우 반복문 종료
    if n < k:
        break
    
    # 나누는 과정 (횟수 +1)
    result += 1
    n //= k

# n이 k보다 작은 경우 1까지 도달하는데 필요한 과정을 result에 더하기
result += (n - 1)
print(result)