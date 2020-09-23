# 유기농 배추

import time
start_time = time.time()

from sys import stdin
input = stdin.readline

def dfs(a, b):
    if a < 0 or a > n-1 or b < 0 or b > m-1:
        return False   
    if graph[a][b] == 1:
        graph[a][b] = 0
        dfs(a+1,b)
        dfs(a-1,b)
        dfs(a,b+1)
        dfs(a,b-1)
        return True
    return False

t = int(input())
result = []
for tc in range(t):
    n,m,k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1
    
    result.append(count)

for r in result:
    print(r)    

end_time = time.time()
print(end_time - start_time)