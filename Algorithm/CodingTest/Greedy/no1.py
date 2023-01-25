# 1이 될 때까지

# 내 풀이 (단순 풀이와 비슷한데 오묘하게 다름 -> 내께 더 빠름)

# import time
# start_time = time.time() # 측정 시작

# # N, K를 공백을 두어 입력받기
# n,k = map(int, input().split())
# count = 0

# while True:
#     # n이 1이면 중지
#     if n == 1:
#         break
#     # n과 k로 떨어지지 않으면 n을 1씩 빼기
#     elif n % k != 0:
#         n -= 1
#         count += 1
#     # n을 k로 나누기
#     else:
#         n //= k
#         count += 1

# print(count)

# end_time = time.time() # 측정 종료
# print("time : ", end_time - start_time) # 수행 시간 출력, N = 100000, K = 543일 때 14.59초 소요

# 단순 풀이

# import time
# start_time = time.time() # 측정 시작

# n, k = map(int, input().split())
# result = 0

# # N이 K 이상이면 K로 계속 나누기
# while n >= k:
#     # N이 K로 나누어 떨어지지 않으면 N에서 1씩 빼기
#     while n % k != 0:
#         n -= 1
#         result += 1
#     # K로 나누기
#     n //= k
#     result += 1

# # 마지막으로 남은 수에 대해서 1씩 빼기
# while n > 1:
#     n -= 1
#     result += 1

# print(result)

# end_time = time.time() # 측정 종료
# print("time :", end_time - start_time) # 수행 시간 출력, N = 100000, K = 543일 때 21.47초 소요

# 효율적인 코드 작성 답안

# import time
# start_time = time.time() # 측정 시작

# # N, K 공백으로 구분하여 입력받기
# n,k = map(int, input().split())
# result = 0

# while True:
#     # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#     print(n)
#     # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # K로 나누기
#     result += 1
#     n //= k
    

# # 마지막으로 남은 수에 대해서 1씩 빼기
# result += (n-1) # n = 1이 되어 반복문이 탈출하면, result에는 n - target + target - 1이 더해진다. 즉, n = 1일 때 result에 더해지는 것은 없다.
# print(result)

# end_time = time.time() # 측정 종료
# print("time : ", end_time - start_time) # 수행 시간 출력, N = 100000, K = 543일 때 4.9초 소요
