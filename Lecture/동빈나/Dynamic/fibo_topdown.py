# 피보나치 수열: 탑다운 다이나믹 프로그래밍

d = [0] * 1000

def fibo(n):
    if n == 1 or n == 2:
        return 1

    if d[n] != 0:
        return d[n]
    
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]

print(fibo(999))