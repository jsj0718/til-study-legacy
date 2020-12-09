from collections import deque

# BFS 소스코드 구현
def bfs(x, y):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # Queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 4가지 방향으로 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽에 부딪힌 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 올바른 길로 갔을 때 값에 1 더하기
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))