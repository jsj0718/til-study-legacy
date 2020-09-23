from collections import deque
from sys import stdin
input = stdin.readline

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_1 = [False for _ in range(n+1)]
visited_2 = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(len(graph)):
    graph[j].sort()

print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited_1)
print()
bfs(graph, v, visited_2)