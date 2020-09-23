# 기존 알람 시간보다 45분 빨리 일어나도록 설정

# 내 풀이

# H, M = list(map(int,input().split()))

# if M >= 45:
#     print(H, M-45)
# elif H != 0 and M < 45:
#     print(H-1, 60-(45-M))
# elif H == 0 and M < 45:
#     print(23, 60-(45-M))

# 모범 답안

# a,b=map(int,input().split())
# print((a-(b<45))%24,(b-45)%60) 
# b<45면 True가 되어 a-1, 또한 24이상이 되면 나머지가 되서 00부터 계산됨.
# -35 % 60 = (-1 * 60 + 25) / 몫 = -1, 나머지 = 25

# 직접 해보기

h, m = map(int, input().split())
print((h-(m<45))%24, (m-45)%60)





