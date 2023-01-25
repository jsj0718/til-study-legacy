# 연결 요소의 개수
# 런타임 에러로 pypy3를 통해 풀이하니 해결

from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
lst = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 이 부분은 해답을 봄
result = 0
# 1~n까지 반복
for j in range(1, n+1):
    # 만약 방문이 안되어있다면,
    if not visited[j]:
        # 한 번 더 함수를 사용
        dfs(graph, j, visited)
        # 쓸 때마다 result 변수에 +1을 한다.
        result += 1
print(result)

