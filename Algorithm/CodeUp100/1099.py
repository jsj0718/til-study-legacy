# [기초-2차원배열] 성실한 개미

# 영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.

# 왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데,
# 그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

# 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다.
# (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

# 이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.

# 미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
# 오른쪽 또는 아래쪽으로만 움직였다.

# 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
# 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
# 더이상 이동하지 않고 그 곳에 머무른다고 가정한다.


# 미로 상자의 테두리는 모두 벽으로 되어 있으며,
# 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

"""
입력 예시

1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""

"""
출력 예시
1 1 1 1 1 1 1 1 1 1
1 9 9 1 0 0 0 0 0 1
1 0 9 1 1 1 0 0 0 1
1 0 9 9 9 9 9 1 0 1
1 0 0 0 0 0 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""

# 내 답안

m = []
for _ in range(10):
    m.append(input().split())

for i in range(1, 9):
    for j in range(1, 9):
        if m[1][1] == '2':
            m[1][1] = '9'
            break
        elif m[1][1] == '0':
            m[1][1] = '9'
        
        if m[i][j] == '9' and (m[i][j+1] == '0' or m[i][j+1] == '2'):
            if m[i][j+1] == '2':
                m[i][j+1] = '9'
                break
            m[i][j+1] = '9'

        elif m[i][j] == '9' and m[i][j+1] == '1':
            if i == 8:
                break
            elif m[i+1][j] == '2':
                m[i+1][j] = 9
                break
            m[i+1][j] = '9'

for x in range(10):
    for y in range(10):
        print(m[x][y], end=' ')
    print()


# 모범 답안

m = []

for _ in range(10):
    m.append([])
    for __ in range(10):
        m[_].append(0)

for i in range(10):
    s = input().split()
    for j in range(10):
        m[i][j] = int(s[j])

x, y = 1, 1
while True:
    if m[x][y] == 0:
        m[x][y] = 9
    elif m[x][y] == 2:
        m[x][y] = 9
        break

    if (m[x+1][y] == 1 and m[x][y+1] == 1) or (x == 8 and y == 8):
        break

    if m[x][y+1] != 1:
        y += 1
    elif m[x+1][y] != 1:
        x += 1
    
for n1 in range(10):
    for n2 in range(10):
        print(m[n1][n2], end=' ')
    print()
