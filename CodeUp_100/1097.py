# [기초-2차원배열] 바둑알 십자 뒤집기

# 부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...
# "십(+)자 뒤집기를 해볼까?"하고 생각했다.
# 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
# n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

# 참고
# 가로 번호, 세로 번호를 사용할 수 있는 2차원 배열을 사용하면
# 이러한 형태를 쉽게 기록하고 사용할 수 있다. 물론 더 확장한 n차원 배열도 만들 수 있다.


# 배열 입력 방법
m = []
for _ in range(19): 
    m.append(input().split()) # 0과 1을 문자열로 입력받는 것을 유의

t = int(input())

for tc in range(t):
    a,b = list(map(int, input().split()))
    for i in range(19): # 행 먼저 바뀜   
        if m[a-1][i] == '0':
                m[a-1][i] = '1'
        else:
            m[a-1][i] = '0'
        for j in range(19): # 그 후 열 바뀜
            if m[j][b-1] == '0':
                m[j][b-1] = '1'
            else:
                m[j][b-1] = '0'

for x in m:
    for y in x:
        print(y, end=' ')
    print()

# # 다른 출력 방법
# for x in range(19):
#     for y in range(19):
#         print(m[x][y], end=' ')
#     print()



# 모범답안

# m=[]
# for i in range(20) :
#     m.append([])
#     for j in range(20) :
#         m[i].append(0)

# for i in range(19) :
#     a=input().split()
#     for j in range(19) :
#         m[i+1][j+1]=int(a[j])
    
# n=int(input())

# for i in range(n) :
#     x,y=input().split()
#     for j in range(1, 20) :
        
#         if m[j][int(y)]==0 :
#             m[j][int(y)]=1
#         else :
#             m[j][int(y)]=0

#         if m[int(x)][j]==0 :
#             m[int(x)][j]=1
#         else :
#             m[int(x)][j]=0

# for i in range(1, 20) :
#     for j in range(1, 20) :
#         print(m[i][j], end=' ')
#     print()