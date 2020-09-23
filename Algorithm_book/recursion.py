# 재귀함수

# 1) 팩토리얼

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# n = int(input())
# print(factorial(n))
    

# 2) 피보나치 수열

# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-2) + fibo(n-1)

# n = int(input())
# print(fibo(n))

# fibonacci

# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)

# for i in range(10):
#     print(fibo(i))


# 최대공약수 (유클리드 호제법)
# def factorization(a,b):
#     if b == 0:
#         return a
#     return factorization(b, a % b)

# print(factorization(216, 38))

# 하노이의 탑


