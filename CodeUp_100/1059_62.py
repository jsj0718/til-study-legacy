# [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기

# n = ~int(input()) # 1은  00000000 00000000 00000000 00000001, ~1은 11111111 11111111 11111111 11111110 = -2
# # 비트단위(bitwise) 연산자 종류
# # ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# # <<(bitwise left shift), >>(bitwise right shift)
# print(n)

# [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기 (둘 다 True면 True, 아니면 False)

# a,b = list(map(int, input().split())) # 3, 5 -> 2진수로 컴퓨터가 인식 -> 011, 101 -> and면 001이므로 1출력
# print(a&b)



# [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기 (하나만 True면 True, 아니면 False)

# a, b = list(map(int, input().split())) # 3, 5 = 011, 101 즉, or이면 111이므로 7 출력
# print(a|b)

# [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기 (다르면 True, 같으면 False)

a, b = list(map(int, input().split()))
print(a^b)