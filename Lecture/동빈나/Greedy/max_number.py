# 주어진 숫자 문자열을 +와 *를 이용해 최대값 구하기

data = input()
# 첫 번째 문자를 숫자로 변경해서 대입
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])

    # 두 수 중에서 하나라도 1보다 작으면 더하고, 아니면 곱하기
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)