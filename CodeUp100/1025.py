# [기초-입출력] 정수 1개 입력받아 나누어 출력하기

# 내 답안

number = list(input())
count = 4
for n in number:
    empty_list = []
    n = n + "0" * count
    empty_list.append(int(n))
    count -= 1
    print(empty_list)

# 모범 답안

n = input()

print("[" + str(int(n[0])*10000) + "]")
print("[" + str(int(n[1])*1000) + "]")
print("[" + str(int(n[2])*100) + "]")
print("[" + str(int(n[3])*10) + "]")
print("[" + str(int(n[4])) + "]")