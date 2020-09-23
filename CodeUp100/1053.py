# [기초-논리연산] 참 거짓 바꾸기

# 내 답안

a = int(input())
# not을 붙이면 int형태에서 bool형태로 변경된다.
# 0(False)이 아닌 모든 수는 True, 그러나 not을 이용하면 0만이 True, 나머지는 False가 된다.
print(int(not a)) 

# 모범답안

a = int(not(bool(int(input())))) # bool을 통해 숫자를 True or False로 바꿀 수 있다.
print(a)


# [기초-논리연산] 둘 다 참일 경우만 참 출력하기

# 내 답안 (if문 사용)
a,b = list(map(int, input().split()))
if a == True and b == True:
    print(1)
else:
    print(0)

# 모범 답안 (and를 이용하면 if문을 사용하지 않아도 된다!)
a, b = list(map(int, input().split()))
a, b = bool(a), bool(b)
z = int(a and b)
print(z)


# [기초-논리연산] 하나라도 참이면 참 출력하기

a, b = list(map(int, input().split()))
a, b = bool(a), bool(b)
z = int(a or b)
print(z)

# [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기

a, b = list(map(int, input().split()))
a, b = bool(a), bool(b)
z = int(a != b)
print(z)

# [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기

a, b = list(map(int, input().split()))
a, b = bool(a), bool(b)
z = int(a == b)
print(z)

# [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기

a, b = list(map(bool,map(int, input().split())))
z = int(not(a or b))
print(z)