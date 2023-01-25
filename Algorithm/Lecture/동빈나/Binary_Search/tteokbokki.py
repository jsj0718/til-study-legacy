# 내 풀이

# def cutting(array, m, start, end):
#     result_list = []
#     while start <= end:
#         mid = (start + end) // 2
#         count = 0
#         for i in array:
#             if i > mid:
#                 count += (i - mid)
#             else:
#                 continue
#         if count >= m:
#             result_list.append(mid)
#             start = mid + 1
#         else:
#             end = mid - 1
#     return max(result_list)

# n,m = map(int, input().split())
# array = list(map(int, input().split()))

# print(cutting(array, m, 0, max(array)))


# 나동빈 풀이
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i >= mid:
            total += (i - mid)

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)    
    
