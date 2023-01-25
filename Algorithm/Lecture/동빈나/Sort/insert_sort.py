array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # 인덱스 i부터 1까지 1씩 감소하면서 반복
    for j in range(i, 0, -1):
        # 한 칸 왼쪽인 것과 비교 (작으면 스와프)
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        # j가 j-1보다 크다면 그 위치에서 스탑
        else:
            break

print(array)