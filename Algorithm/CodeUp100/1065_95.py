# numbers = list(map(int, input().split()))
# for n in numbers:
#     if n % 2 == 0: # 조건이면 출력함. 조건이 아니면 넘어감.
#         print(n)

# numbers = list(map(int, input().split()))
# for n in numbers:
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# n = int(input())
# if n < 0:
#     print("minus")      
# else:
#     print("plus")

# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# n = int(input())
# if n >= 90:
#     print("A")
# elif n >= 70:
#     print("B")
# elif n >= 40:
#     print("C")
# else:
#     print("D")


# s = input()

# if s == "A":
#     print("best!!!")
# elif s == "B":
#     print("good!!")
# elif s == "C":
#     print("run!")
# elif s == "D":
#     print("slowly~")
# else:
#     print("what?")

# n = int(input())
# if n == 12 or n == 1 or n == 2:
#     print("winter")
# elif n == 3 or n == 4 or n == 5:
#     print("spring")
# elif n == 6 or n == 7 or n == 8:
#     print("summer")
# else:
#     print("fall")

# numbers = list(map(int, input().split()))
# for n in numbers:
#     if n == 0:
#         break
#     print(n)

# t = int(input())
# numbers = list(map(int,input().split()))
# for n in numbers:
#     print(n)

# n = int(input())
# while n > 0:
#     n -= 1
#     print(n)
    

# s = ord(input())
# for i in range(97, s+1):
#     print(chr(i), end=' ')


# s = ord(input())
# i = ord("a")
# while i <= s:
#     print(chr(i), end=' ')
#     i += 1 


# n = int(input())
# sum_even = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         sum_even += i
# print(sum_even)

# s_list = list(input().split())
# for s in s_list:
#     print(s)
#     if s == "q":
#         break

# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s += i
#     if s >= n:
#         print(i)
#         break

# n = int(input())
# i = 0
# s = 0
# while s<n:
#     i += 1
#     s += i
# print(i)

# n, m = list(map(int, input().split()))
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i, j)

# -----------------------------------------------------------------------------------------------------------------
# [기초-종합] 16진수 구구단
# n = int(input(),16) # 16진수로 입력을 받음
# for i in range(int("1", 16), int("10", 16)): # 범위를 1~F까지 설정
#     print("{:X}*{:X}={:X}".format(n, i, (n*i))) # {:X}로 16진수 표현 가능
# -----------------------------------------------------------------------------------------------------------------

# n = int(input())
# for i in range(1, n+1):
#     if i % 3 == 0:
#         i = "X"
#     print(i, end=' ')

# a, b, c = list(map(int,input().split()))
# cnt = 0
# for x in range(a):
#     for y in range(b):
#         for z in range(c):
#             print(x,y,z)
#             cnt += 1
# print(cnt)

# h, b, c, s = list(map(int, input().split()))
# print("{:.1f} MB".format((h*b*c*s/8)/(1024**2)))

# w, h, b = list(map(int, input().split()))
# print("{:.2f} MB".format((w*h*b/8)/(1024**2)))


# n = int(input())
# i = 0
# s = 0
# while s<n:
#     i += 1
#     s += i
# print(s)


# n = int(input())
# for i in range(1, n+1):
#     if i % 3 == 0:
#         continue
#     print(i)

# -----------------------------------------------------------------------------------------------------------------
# 등차수열

# a, d, n = list(map(int, input().split()))
# number = a + d * (n-1)
# print(number)

# 등비수열

# a, r, n = list(map(int, input().split()))
# # 반복문 활용
# for _ in range(n-1):
#     a *= r
# print(a)
# # 수열 식 활용
# number = a * (r ** (n-1))
# print(number) 
# -----------------------------------------------------------------------------------------------------------------

# a, m, d, n = list(map(int, input().split()))
# for _ in range(n-1):
#     a *= m
#     a += d
# print(a)

# -----------------------------------------------------------------------------------------------------------------
# a, b, c의 최소공배수를 if문으로 풀이
# a,b,c = list(map(int,input().split()))
# day = 1
# while day % a != 0 or day % b != 0 or day % c != 0:
#     day += 1
# print(day)
# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------
# 내 풀이

# t = int(input())
# numbers = list(map(int, input().split()))
# choice = list(range(1,24))
# for i in range(1, 24):
#     cnt = 0
#     if i in numbers:
#         cnt += numbers.count(i)
#         choice[i-1] = cnt
#     else:
#         choice[i-1] = 0

# for x in choice:
#     print(x, end=' ')

# 모범 답안

# t = int(input())
# numbers = list(map(int, input().split()))
# arr = []
# for i in range(1,24):
#     arr.append(0)

# for j in numbers:
#     arr[j-1] += 1

# for k in arr:
#     print(k, end=' ')
# -----------------------------------------------------------------------------------------------------------------

# t = int(input())
# numbers = list(map(int, input().split()))
# for i in range(t):
#     print(numbers[t-(i+1)], end=' ')

# t = int(input())
# n = list(map(int,input().split()))
# fast_n = n[0]
# for i in range(len(n)):
#     if n[i] < fast_n:
#         fast_n = n[i]
# print(fast_n)