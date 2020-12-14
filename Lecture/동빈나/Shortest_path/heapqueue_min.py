"""
heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. The order is adjusted, so as heap structure is maintained.
heappop(heap) :- This function is used to remove and return the smallest element from heap. The order is adjusted, so as heap structure is maintained.
"""

import heapq

# 오름차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
 
result = heapsort([1, 3, 5, 7, 8, 2, 4, 6, 9, 0])
print(result)

