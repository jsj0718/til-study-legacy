# 양 문제

T = int(input())

for i in range(T):
    print(f"#{i+1} ", end='')

    sheep = int(input())
    sheeps = 0
    n = 1
    number_set = set()
    for i in range(10):
        while i not in number_set: # not in을 써야 요소가 없을 때 while문에서 True가 되어 루프 사용 가능.
            sheeps = sheep * n
            sheeps_set = set(map(int,str(sheeps)))
            number_set = number_set | sheeps_set
            n += 1
    print(sheeps)
