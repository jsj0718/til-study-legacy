a = int(input())

for i in range (a):
    print(f'#{i+1}', end = ' ')
    b = int(input())

    # c를 list로 한 번에 받은 다음 .sort로 정렬
    c = list(map(int, input().split()))
    c.sort()

    # c의 각 성분을 문자열로 변환 후 구분자를 ' '로 지정.
    print(' '.join(map(str, c)))