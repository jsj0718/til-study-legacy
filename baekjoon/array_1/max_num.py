# 9개의 정수가 주어지고, 그 중에서 최댓값과 그 위치를 찾는 문제

n_list = []
idx = 0

for i in range(9):
    n = int(input())
    n_list.append(n)

for j in range(len(n_list)):
    if n_list[idx] < n_list[j]:
        idx = j

print(n_list[idx])
print(idx+1)