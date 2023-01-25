# 각 자리수 합 함수 정의
def sum_digit(number):
    result = 0
    for i in range(len(number)):
        result += int(number[i])
    return result

# 각 자리수 곱 함수 정의
def mult_digit(number):
    result = 1
    for i in range(len(number)):
        result *= int(number[i])
    return result

# 비교 함수 정의
def score(pobi, crong):
    # 포비와 크롱의 각 페이지 자리수의 합과 곱 리스트 생성
    output_pobi = []
    output_crong = []

    # 예외사항 (왼쪽 페이지 홀수가 아닌 경우, 양쪽 페이지 차가 1이 아닌 경우)
    if (pobi[0] % 2 != 1) or (crong[0] % 2 != 1) or (pobi[1] - pobi[0] != 1) or (crong[1] - crong[0] != 1):
        return -1 
    # 포비의 output 리스트 정의
    for item in pobi:
        output_pobi.append(sum_digit(str(item)))
        output_pobi.append(mult_digit(str(item)))
    # 크롱의 output 리스트 정의
    for item in crong:
        output_crong.append(sum_digit(str(item)))
        output_crong.append(mult_digit(str(item)))
    # 포비가 이길 경우 1
    if max(output_pobi) > max(output_crong):
        return 1
    # 크롱이 이길 경우 2
    elif max(output_pobi) < max(output_crong):
        return 2
    # 비길 경우 0
    elif max(output_pobi) == max(output_crong):
        return 0

pobi = [99, 102]
crong = [211, 212]

print(score(pobi, crong))