# virus, 백준 2606번 문제

from sys import stdin
input = stdin.readline

n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
lst = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)

print(visited.count(True)-1)