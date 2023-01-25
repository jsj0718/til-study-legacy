# [기초-2차원배열] 바둑판에 흰 돌 놓기

# 내 풀이
# n = int(input())
# arr = [[0]*19 for _ in range(19)]
# for __ in range(n):
#     a,b = list(map(int, input().split()))
#     arr[a-1][b-1] = 1
# for i in arr:
#     for j in i:
#         print(j, end=' ')
#     print()

# 모범 답안
# m=[]
# for i in range(20) :
#     m.append([])
#     for j in range(20) :
#         m[i].append(0)
    
# n=int(input())
# for i in range(n) :
#     x,y=input().split()
#     m[int(x)][int(y)]=1

# for i in range(1, 20) :
#     for j in range(1, 20) :
#         print(m[i][j], end=' ')
#     print()


m = []
for i in range(19):
    m.append([])
    for j in range(19):
        m[i].append(0)        

n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    m[a-1][b-1] = 1

for x in m:
    for y in x:
        print(y, end=' ')
    print()