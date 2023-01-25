import heapq

# 내림차순 힙 정렬 (Heap Sort), 오름차순과 차이는 push와 pop 때 부호를 붙이는 것 차이
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽인
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result = heapsort([1, 3, 5, 7, 8, 2, 4, 6, 9, 0])
print(result)