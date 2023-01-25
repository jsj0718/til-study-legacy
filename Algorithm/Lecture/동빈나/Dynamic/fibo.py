# 피보나치 함수 재귀적 구현
def fibo(n):
    print('f(' + str(n) +')', end=' ')
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

fibo(6)