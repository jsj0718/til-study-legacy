from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

# 배열 선언
array = [1, 2, 3, 3, 3, 3, 4, 4, 7, 8]

# 값이 4인  데이터 개수 출력(6:8)
print(count_by_range(array, 4, 4))
# 값이 -1부터 3 사이인 데이터 개수 출력 (0:6)
print(count_by_range(array, -1, 3))