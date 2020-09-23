# 00:00:00 부터 N:00:00 까지 3이 포함되는 경우의 수 계산하기

# N(시간) 입력받기
n = int(input())
# count할 변수 선언하기
result = 0

# 3중 for문을 통해 00:00:00부터 N:59:59까지의 시간 구하기
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 시,분,초를 str()을 이용하여 문자열로 합친 후, "3"이 포함되어 있는지 확인하기
            if "3" in (str(i)+str(j)+str(k)):
                # 3이 포함되면 result에 1 더하기
                result += 1

print(result) # 결과 출력하기