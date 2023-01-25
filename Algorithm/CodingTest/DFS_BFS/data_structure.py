# 스택: 선입후출 구조(박스 쌓기)

# stack = []

# # 5-2-3-7-삭제-1-4-삭제
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack) # 최하단부터 출력
# print(stack[::-1]) # 최상단부터 출력

# # 큐 : 선입선출 구조(대기줄)

# # deque는 stack과 queue의 장점을 모두 채택한 것 (데이터를 넣고 빼는 속도가 리스트보다 효율적, queue 라이브러리보다 간단함)
# from collections import deque # 큐 구현 시 collections 모듈에서 제공하는 deque 자료구조 이용하기
# queue = deque()

# # 5-2-3-7-삭제-1-4-삭제
# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft() # 먼저 들어온 순서대로 리스트가 생성되므로, 왼쪽 원소를 삭제해야 선입선출 형태가 된다.
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue) # 먼저 들어온 순서대로 출력
# queue.reverse() # 역순으로 바꾸기
# print(queue) # 나중에 들어온 원소부터 출력

# 재귀 함수: 자기 자신을 다시 호출하는 함수

# 무한 호출
# def recursive_function_1():
#     print("재귀 함수를 호출합니다.")
#     recursive_function_()

# recursive_function_1()

# 종료 조건이 있는 재귀 함수 (선입후출 과정, 재귀 함수는 컴퓨터 내부적으로 스택 자료구조와 동일)
# def recursive_function_2(n):
#     if n == 100:
#         return
#     print("{}번째 재귀 함수에서 {}번째 재귀 함수를 출력합니다.".format(n, n+1))
#     recursive_function_2(n+1)
#     print(n, "번째 재귀 함수를 종료합니다.")

# recursive_function_2(1)

# # 팩토리얼 예제 - 1 (반복적 구현)
# def factorial(n):
#     result = 1
    
#     # 1부터 n까지 차례대로 곱하기
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(factorial(5))


# # 팩토리얼 예제 - 2 (재귀적 구현)
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n-1)

# n = 5
# print(factorial(n))

# 반복문 vs 재귀 함수
# 재귀함수가 반복문보다 간결하다.(수학적 재귀식을 그대로 옮겼기 때문) -> 다이나믹 프로그래밍으로 이어진다.