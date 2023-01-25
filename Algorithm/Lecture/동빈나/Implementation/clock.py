# 시각 문제 (3을 포함하는 시간의 총 횟수 구하기)
# 하루는 86,400초이므로 완전탐색으로도 충분히 구할 수 있다.

h = int(input())
count = 0

# 시, 분, 초를 1씩 증가시켜서 3을 포함하는지 확인하기
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)