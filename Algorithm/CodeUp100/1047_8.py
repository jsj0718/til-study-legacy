# [기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기

# n = int(input())
# print(n<<3) # n * 2^2, <<는 2^을 의미


# [기초-비트시프트연산] 한 번에 2의 거듭제곱 배로 출력하기

a,b = list(map(int,input().split()))
print(a<<b) # a * 2^b 와 동일