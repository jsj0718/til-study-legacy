def dfs(x, y):
    # 범위를 벗어나는 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 재귀 호출은 return값을 사용하지 않는다. (값이 1로만 바뀌고 True 반환은 하지 않는다.)
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    # 그 외 경우
    return False

n, m = map(int, input().split())

# 2차원 배열 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 총 0의 덩어리 수
result = 0

# n * m 배열의 요소 하나씩 탐색하기
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)