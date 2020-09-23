# 세 정수를 곱한 후 0~9까지 각 몇 개씩 들어갔는지 확인하는 문제

num1 = int(input())
num2 = int(input())
num3 = int(input())
num_mult = str(num1 * num2 * num3)
for i in range(10):
    if str(i) in num_mult:
        print(num_mult.count(str(i)))
    else:
        print(0)