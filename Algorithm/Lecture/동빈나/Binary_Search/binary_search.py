# 찾고자하는 원소의 위치 출력

# 재귀적 구현

# def binary_search(array, target, start, end):
#     if start > end:
#         return None

#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)

# n, target = map(int, input().split())
# array = list(map(int, input().split()))
# array.sort()

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)

# 반복문 구현

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None 

n, target = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
