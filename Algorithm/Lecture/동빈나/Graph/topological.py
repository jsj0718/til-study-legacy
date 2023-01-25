# # 위상 정렬 by 나동빈

# from collections import deque

# # 노드의 개수와 간선의 개수 입력 받기
# v, e = map(int, input().split())
# # 모든 노드에 대한 진입차수는 0으로 초기화
# indegree = [0] * (v + 1)
# # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
# graph = [[] for _ in range(v + 1)]

# # 방향 그래프의 모든 간선 정보를 입력 받기
# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)  # 정점 A에서 B로 이동 가능
#     # 진입 차수 1 증가
#     indegree[b] += 1

# # 위상 정렬 함수
# def topological_sort():
#     result = [] # 알고리즘 수행 결과를 담을 리스트
#     q = deque() # 큐 기능을 위한 deque 라이브러리 사용
#     # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
#     for i in range(1, v + 1):
#         if indegree[i] == 0:
#             q.append(i)
#     # 큐가 빌 때까지 반복
#     while q:
#         # 큐에서 원소 꺼내기
#         now = q.popleft()
#         result.append(now)
#         # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
#         for i in graph[now]:
#             indegree[i] -= 1
#             # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
#             if indegree[i] == 0:
#                 q.append(i)
#     # 위상 정렬을 수행한 결과 출력
#     for i in result:
#         print(i, end=' ')

# topological_sort()


# 내가 정리한 것

from collections import deque

# 노드의 개수, 간선의 개수 입력 받기
v, e = map(int, input().split())
# 모든 노드의 진입차수 테이블 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담을 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력 받기
for i in range(e):
    a, b = map(int, input().split())
    # A -> B로 이동 (B의 진입차수 +1)
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 함수 선언
def topological_sort():
    # 정렬 결과를 담을 리스트 초기화
    result = []
    # 큐 선언 (deque 라이브러리 사용)
    q = deque()
    # 진입차수가 0인 노드를 큐에 추가
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 꺼내어 현재 노드 설정 및 결과 리스트에 담기
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들 꺼내기
        for i in graph[now]:
            # 연결된 노드의 진입차수 -1
            indegree[i] -= 1
            # 진입차수가 0인 노드 큐에 담기
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬 수행 결과 출력
    for i in result:
        print(i, end=' ')

topological_sort()

"""
Test Case

첫 번째 줄은  v, e 
두 번째 줄부터 a, b (a -> b)
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""