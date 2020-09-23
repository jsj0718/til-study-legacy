# 상하좌우 문제

# 내 풀이 (하나씩 풀어서 푸는 습관이 아직 남아있다.)

# n = int(input())
# move = input().split()
# a,b = 1,1

# for i in move:
#     if i == "R":
#         b += 1
#         if b > n:
#             b -= 1
#     elif i == "L":
#         b -= 1
#         if b < 1:
#             b += 1
#     elif i == "D":
#         a += 1
#         if a > n:
#             a -= 1
#     elif i == "U":
#         a -= 1
#         if a < 1:
#             a += 1

# print(a, b)
    
# 효율적 풀이

n = int(input())
# 공백을 두어 좌표 이동 계획 입력받기
plans = input().split()
# x, y 초기값 변수 선언
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
move_type = ["R", "L", "U", "D"]

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    # x, y의 좌표가 1보다 작거나 n보다 크면, continue를 통해 x,y 좌표 최신화를 건너뛴다.
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue

    x, y = nx, ny

print(x,y)