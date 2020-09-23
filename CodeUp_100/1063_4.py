# [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기 (3항 연산자 이용)

# a,b = list(map(int, input().split()))
# print(a if a>b else b) # 3항 연산자 -> [True Value] if [Condition] else [False Value]

# [기초-삼항연산] 정수 3개 입력받아 가장 작은 수 출력하기

a,b,c = list(map(int, input().split()))
print((a if a<b else b) if (a if a<b else b)<c else c)