# 문제
"""
n = input (26) -> 1. (2+6 = 8 -> 68) -> 2. (6+8 = 14 -> 84) -> 3. (8+4 = 12 -> 42) -> 4. (4+2 = 6 -> 26) 

단, 10보다 작으면 앞에 0을 붙인다. 
"""
# 진표 풀이

# num = input()
# if len(num) == 1:
#     first = '0' + num
# else:
#     first = num
# cycle = 0
# while True:
#     if len(num) == 1:
#         num = '0' + num
#     num = num[1] + str(int(num[0])+int(num[1]))[-1]
#     cycle += 1
#     if num == first:
#         print(cycle)
#         break

# 내 풀이 (1)

# num = int(input())
# num_list = list(str(num))
# num_sum = str(sum(list(map(int,num_list)))).zfill(2)
# next_num = int(num_list[1] + num_sum[1])
# cycle_cnt = 0

# while num != next_num:
#     num = next_num
#     num_list = list(str(num))
#     num_sum = str(sum(list(map(int,num_list)))).zfill(2)
#     next_num = int(num_list[1] + num_sum[1])
#     cycle_cnt += 1

# print(cycle_cnt)

# 내 풀이 (2)

# num = int(input())
# print(num, type(num))

# num_list_str = list(str(num))
# print(num_list_str, type(num_list_str))

# num_list_int = list(map(int,list(str(num))))
# print(num_list_int, type(num_list_int))

# num_list_sum = str(sum(num_list_int)).zfill(2)
# print(num_list_sum, type(num_list_sum))

# new_num = int(num_list_str[1] + num_list_sum[1])
# print(new_num, type(new_num))

# cnt = 0

# while num != new_num:
#     num = new_num
#     num_list_str = list(str(num))
#     num_list_int = list(map(int,list(str(num))))
#     num_list_sum = str(sum(num_list_int)).zfill(2)
#     new_num = int(num_list_str[1] + num_list_sum[1])
#     cnt += 1
# print(cnt)


num = input()
if len(num) == 1:
    first = num.zfill(2)
else:
    first = num
cycle_cnt = 0

while True:
    if len(num) == 1:
        num = num.zfill(2)
    num = num[1] + str(int(num[0])+int(num[1]))[-1] # [-1]은 리스트의 마지막 요소의 인덱스이다. num = [1]인 리스트에서 num[0]과 num[-1]의 값은 동일
    cycle_cnt += 1
    if first == num:
        print(cycle_cnt)
        break

