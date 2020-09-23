# 게임 개발

# # 맵 배열인 N X M 입력하기
# n,m = map(int, input().split())
# # 좌표 a, b와 방향 d 입력하기
# a,b,d = map(int, input().split())

# # 공식 맵 입력하기
# office_map = []
# for _ in range(n):
#     office_map.append(list(map(int, input().split())))

# # 유저 맵 등록하기
# user_map = [[0]*m for _ in range(n)]
# user_map[a][b] = 1

# da = [-1, 0, 1, 0]
# db = [0, 1, 0, -1] 

# def turn_left():
#     global d
#     d -= 1
#     if d == -1:
#         d = 3

# turn_time = 0
# count = 1

# while True:
#     turn_left()
#     na = a + da[d]
#     nb = b + db[d]

#     if office_map[na][nb] == 0 and user_map[na][nb] == 0:
#         user_map[na][nb] = 1
#         a = na
#         b = nb
#         count += 1
#         turn_time = 0
#         continue
#     else:
#         turn_time += 1

#     if turn_time == 4:
#         na = a - da[d]
#         nb = b - db[d]

#         if office_map[na][nb] == 0:
#             a = na
#             b = nb
#         else:
#             break
#         turn_time = 0

# print(count)


# 정식 풀이

import time
start_time = time.time()

# N X M 배열을 만들기 위한 N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 좌표 a, b와 방향 d를 입력받기
a, b, d = map(int, input().split())

# 입력받는 맵을 공식 맵으로 선언하고 입력받기
office_map = []
for _ in range(n):
    office_map.append(list(map(int, input().split())))

# 유저가 이동한 맵을 기록하는 유저 맵을 선언하기
user_map = [[0]*m for _ in range(n)]
# 가본 곳은 1로 입력하기
user_map[a][b] = 1

# 북, 서, 남, 동에 따른 a와 b의 좌표 이동 리스트 만들기
da = [-1, 0, 1, 0] # a는 상하
db = [0, 1, 0, -1] # b는 좌우

# 왼쪽으로 방향을 이동하는 함수를 만들기
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
count = 1 # 첫 위치를 가본 곳으로 치기 때문에 count = 1로 선언
turn_time = 0 # 왼쪽으로 회전하는 횟수

while True:
    # 왼쪽으로 회전
    turn_left()
    na = a + da[d]
    nb = b + db[d]
    # 회전 후 가보지 않은 곳이면 이동
    if user_map[na][nb] == 0 and office_map[na][nb] == 0:
        user_map[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_time = 0
        continue  # continue를 넣음으로써 연산 속도가 굉장히 빨라진다.
    # 회전 후 정면에 바다나 가보지 않은 곳이 없을 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없을 경우
    if turn_time == 4:
        na = a - da[d]
        nb = b - db[d]
        # 뒤로 갈 수 있으면 이동
        if office_map[na][nb] == 0:
            a = na
            b = nb
            turn_time = 0  # 내가 넣은 위치 (나동빈 위치보다 더 빠른 속도, 테스트가 적어 결과에 차이가 있는지는 모르겠다.)
        else:
            break
        # turn_time = 0  # 나동빈이 넣은 위치
print(count)

end_time = time.time()
print(end_time - start_time)

