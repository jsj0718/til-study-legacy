# 좌표 주어질 때, 사분면 구하는 문제

# 내 답안
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else:
#     print(4)


# 다른 답안
a,b  = int(input()), int(input())
print('3421'[(a>0) + (b>0) * 2]) # bool * num를 하면 bool은 1(True) or 0(False의 값으로 계산된다.