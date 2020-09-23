# while 문 a+b 이용 문제 (while의 구조를 알 수 있음)
while True:
    a, b = list(map(int, input().split()))
    if a != 0 and b != 0:
        print(a+b)
    else:
        break