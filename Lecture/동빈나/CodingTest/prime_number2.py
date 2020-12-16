import math

# 소수 판별 함수 (2 이상의 자연수)
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나눠 떨어진다면
        if x % i == 0:
            # 소수 X
            return False
    # 소수 O
    return True

result = []

for i in range(2, 101):
    if is_prime_number(i):
        result.append(i)
    
print(len(result))