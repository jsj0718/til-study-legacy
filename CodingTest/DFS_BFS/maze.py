from collections import deque
# N과 M을 공백을 두어 입력받기
n, m = map(int, input().split())
# 2차원 리스트 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# x, y 좌표의 상하좌우 이동 리스트 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 끝날 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 주어진 범위 바깥으로 나가면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물을 만나면 무시
            if graph[nx][ny] == 0:
                continue
            # 새로운 좌표가 1일 때
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[n-1][m-1]

print(bfs(0,0))