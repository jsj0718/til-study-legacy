# 전보 문제
# 한 도시에서 다른 도시로 편지를 보낼 때 편지를 받은 도시의 수와 총 걸린 시간을 구하는 문제

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))
    # 큐가 빌 때까지 반복
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 노드의 개수, 간선의 개수, 시작 지점 입력받기
n, m, c = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 선언
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x -> y 로 가는데 필요한 비용 z
    graph[x].append((y, z))

    
dijkstra(c)

# 도달 가능한 도시 개수 카운트
count = 0
# 도달 가능한 도시들 중에서 가장 멀리 있는 도시의 최단 거리
result = 0

for d in distance:
    # 도달 가능한 도시인 경우
    if d != INF:
        count += 1
        result = max(result, d)

# 시작 노드는 제외이므로 -1하기
print(count - 1, result)