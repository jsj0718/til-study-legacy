# 왕실의 나이트

# # 내 풀이 (정말 돌아가게만 짠 코드)
# s = input()
# # 갈 수 있는 좌표를 리스트에 튜플 형식으로 저장하기(힌트 받음)
# steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
# count = 0
# s[0] = ord(s[0])
# s[1] = int(s[1])

# for step in steps:
#     s[0] += step[0]
#     s[1] += step[1]
#     if s[0] < ord("a") or s[0] > ord("h") or s[1] < 1 or s[1] > 8:
#         s[0] -= step[0]
#         s[1] -= step[1]
#         continue
#     else:
#         count += 1
#     s[0] -= step[0]
#     s[1] -= step[1]

# print(count)

# 효율적인 풀이
import time
start_time = time.time()

# 좌표 입력받기
data = input()
# 행(row)과 열(column)로 좌표 나누기
row = int(data[1])
column = ord(data[0]) - ord('a') + 1
# 나이트의 이동 경로 경우의 수를 리스트에 튜플 형식으로 입력하기
steps = [(-2,-1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
count = 0 # 경우의 수 카운트 변수 선언

for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]

    # if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8: # 8X8 배열에서 벗어나면 Continue(c2 입력 시 1.88초)
    #     continue
    # else:
    #     count += 1

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8: # 8X8 배열 안에 있으면 count에 1 더하기(c2 입력 시 1.57초)
        count += 1

print(count)

end_time = time.time()
print("time : ", end_time - start_time)
