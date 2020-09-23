# 숫자 카드 게임

# # 내 풀이 (2차원 배열 이용)
# # 2차원 배열 형성
# a,b = map(int, input().split())
# m = []
# m_min = []
# for _ in range(a):
#     m.append([])
#     for __ in range(b):
#         m[_].append(0)

# for i in range(a):
#     data = list(map(int, input().split())) # 데이터 입력 받기
#     for j in range(b):
#         m[i][j] = data[j] # 데이터를 배열에 입력

# for row in m: # 각 행을 반복
#     m_min.append(min(row)) # 각 행에서 최소값을 새로운 배열에 추가

# print(max(m_min)) # 최소값을 모아놓은 배열 중 최대값을 출력

# # min() 함수 이용
# # N, M을 공백으로 구분하여 입력받기

# n,m = map(int, input().split())
# result = 0

# # 한 줄씩 입력받아 확인
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # 가장 작은 수들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)

# print(result) # 최종 답안 출력

# 2중 for문을 이용한 풀이

# N, M을 공백으로 구분하여 받기
n, m = map(int, input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for d in data:
        min_value = min(min_value, d)
    # 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result) # 최종 답안 출력