# 음료수 얼려 먹기

# N과 M 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트 맵 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# DFS 함수 정의하기
def dfs(x, y):
    # 범위를 벗어나면 즉시 종료하기
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 방문하지 않았다면,
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우 재귀 호출
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)