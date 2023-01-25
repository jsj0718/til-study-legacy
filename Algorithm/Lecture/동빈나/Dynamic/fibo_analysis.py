# Memoization을 이용하는 경우 피보나치 수열의 시간 복잡도는 O(N)
d = [0] * 100

def fibo(n):
    print('f(' + str(n) +')', end=' ')
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

fibo(6) # f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)
