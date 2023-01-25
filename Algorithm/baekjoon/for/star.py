# 실습 1

# n = int(input())

# for i in range(1, 2*n):
#     if i <= n:
#         print("*" * (n-(n-i)))
#     else:
#         print("*" * (n+(n-i)))

# 실습 2

# 출력 양식 오류 (공백 고려 X)

# n = int(input())

# for i in range(1, 2*n):
#     if i <= n:
#         print(("*" * (2*n - (2*i-1))).ljust(2*n-1)) # str.center(int(칸수), " "(채울 내용)) -> 가운데 정렬
#     else:
#         print(("*" * ((2*i+1)-2*n)).center(2*n-1))

# 실습 2 정답

# n = int(input())

# for i in range(1, 2*n):
#     if i <= n:
#         print(("*" * (2*n-(2*i-1))+' ').rjust(2*n-i+1)) # 오른쪽 공백 1자리를 위해 문자열에 ' '을 더함
#     else:
#         print(("*" * ((2*i+1)-2*n)+' ').rjust(i+1))


# 실습 3

n = int(input())

for i in range(1, n+1): # 3 입력시, 총 3번을 반복하라!
    if n == 1:
        print("* ")
    elif n % 2 == 1:
        print("* " * ((n+1)//2))
        print(" " + "* " * (n//2))
    else:
        print("* " * ((n+1)//2))
        print(" " + "* " * (n//2))
