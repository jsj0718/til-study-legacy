# [기초-비교연산] 두 정수 입력받아 비교하기1(나는 if문 활용, 모범답안은 True = 1, False = 0을 이용)

a,b = list(map(int, input().split()))
z = int(a>b) # True를 int로 바꾸면 1, False는 0
print(z)

# [기초-비교연산] 두 정수 입력받아 비교하기2

a,b = list(map(int, input().split()))
z = int(a == b)
print(z)

# [기초-비교연산] 두 정수 입력받아 비교하기3

a,b = list(map(int, input().split()))
z = int(a <= b)
print(z)

# [기초-비교연산] 두 정수 입력받아 비교하기4

a,b = list(map(int, input().split()))
z = int(a != b)
print(z)