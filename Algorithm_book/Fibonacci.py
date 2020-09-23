# 피보나치 수열 문제(0, 1, 1, 2, 3, 5, 8 ...) (재귀함수)

# 내가 푼 풀이
# n = int(input())
# a = [0, 1]
# for i in range(n):
#     b = a[i] + a[i+1]
#     a.append(b) # append 함수는 return이 없어 None으로 출력, 이처럼 표현해야함.
# print(a)

# 문제 해설

def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

for i in range(10):
    print(f(i))