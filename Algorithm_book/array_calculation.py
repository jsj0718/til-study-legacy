# 배열의 합

# def li_sum(li, n):
#     if n <= 0 or n >= len(li):
#         return 0
#     return li[n-1] + li_sum(li, n-1)

# li = [1,2,3,4,5,6,7,8,9,10]
# print(li_sum(li, 9))


# 0~n까지의 합

# def sum_n(n):
#     if n == 0:
#         return n
#     return n + sum_n(n-1)

# print(sum_n(10))


# 팩토리얼

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(1))


# x^n 구현

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print(power(2,9))