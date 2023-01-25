# n개의 정수가 주어질 때, 그 중에서 최대값, 최소값을 구하는 문제

n = int(input())
array = list(map(int, input().split()))
max_num = array[0]
min_num = array[0]
for i in range(n):
    if min_num > array[i]:
        min_num = array[i]
    elif max_num < array[i]:
        max_num = array[i]
    
print(min_num, max_num)