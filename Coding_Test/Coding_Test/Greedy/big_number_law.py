# 큰 수의 법칙
# N개의 data를 받고, 가장 큰 수 K번 + 두 번째로 큰 수 1번 식으로 반복하여 M번만큼 더하여 result를 구하는 문제이다.

# 단순한 방법으로 풀이

# # N, M, K를 공백으로 구분하여 받기
# n, m, k = map(int, input().split())
# # N개의 수를 공백으로 구분하여 받기
# data = list(map(int, input().split()))

# data.sort() # 입력받은 수들 정렬하기
# first = data[-1] # 가장 큰 수
# second = data[-2] # 두 번째로 큰 수

# result = 0

# while m > 0:
#     for i in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0: # m이 0이면 탈출
#             break
#         result += first
#         m -= 1 # 더할 때마다 1씩 빼기
#     if m == 0: # m이 0이면 탈출
#         break
#     result += second # K번 더한 후 두 번째로 큰 수 한 번 더하기
#     m -= 1 # 더할 때마다 1씩 빼기

# print(result)


# 다른 풀이-1 (by 세진)
# n,m,k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[-1]
# second = data[-2]

# result = (first * k + second) * (m // (k+1)) + first * (m % (k+1))
# print(result)

# 다른 풀이-2 (by 동빈나)
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k
count += m % (k+1)

result = first * count # 가장 큰 수 더하기
result += second * (m-count) # 두 번째로 큰 수 더하기

print(result) # 답안 출력