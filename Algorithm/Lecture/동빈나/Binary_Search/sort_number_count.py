from bisect import bisect_left, bisect_right

def count_number(array, x):
    if x in array:
        left_index = bisect_left(array, x)
        right_index = bisect_right(array, x)
        return right_index - left_index
    else:
        return -1

n, x = map(int, input().split())
array = list(map(int, input().split()))
print(count_number(array, x))