# 최대공약수 구하는 문제(재귀함수)

def fac(a,b):
    if b == 0:
        return a
    return fac(b, a % b)

a = int(input())
b = int(input())
c = fac(a,b)
print(c)