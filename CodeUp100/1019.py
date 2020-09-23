# [기초-입출력] 연월일 입력받아 그대로 출력하기

# 내 풀이

# year, month, day = input().split(".")
# print("{0:04d}.{1:02d}.{2:02d}".format(int(year), int(month), int(day)))

# 모범 답안
# a, b, c = input().split(".")
# print("{:04d}".format(int(a)), end='.')
# print("{:02d}".format(int(b)), end='.')
# print("{:02d}".format(int(c)))

a, b, c = input().split(".")
print("%04d" % int(a), end='.')
print("%02d" % int(b), end='.')
print("%02d" % int(c))