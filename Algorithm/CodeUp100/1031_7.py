# [기초-출력변환] 10진 정수 1개 입력받아 8진수로 출력하기

# n = int(input())
# print("%o" % n) # %o는 8진수 변환

# [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1

# n = int(input())
# print("%x" % n) # %x는 16진수 변환

# n = int(input())
# print("%X" % n) # x를 대문자 X로 하면 출력도 대문자로 된다. / upper()는 대문자, lower()는 소문자 함수를 이용해도 된다.


# [기초-출력변환] 8진 정수 1개 입력받아 10진수로 출력하기
# n = int(input(), 8) # int(10진수, x) -> 10진수를 x진수로 바뀜. (n이 x진수로 입력됨.)
# print(n) # 출력은 10진수로 됨.

# [기초-출력변환] 16진 정수 1개 입력받아 8진수로 출력하기
# n = int(input(), 16)
# ans = oct(n)
# print(format(n, 'x')) # format(n, 'b')에서 'b'는 2진수로 출력, 'o'는 8진수, 'd'는 10진수, 'x'는 16진수이다.

# 파이썬 2진수, 8진수, 16진수 변환 사이트 : https://deepflowest.tistory.com/30


# 아스키 코드 출력 (A -> 65)
# s = input()
# print(ord(s))

# 아스키 코드 입력받아 문자 출력 (65 -> A)
s = int(input())
print(chr(s))

# a를 입력받아 b 출력하기

n = ord(input()) # a를 입력받으면 ord()에 의해 97로 치환
print(chr(n+1)) # 97+1이 chr()에 의해 b로 치환