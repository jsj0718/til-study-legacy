# 소수 판별 함수 (2 이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (X - 1)까지의 모든 수를 확인
    for i in range(2, x):
        # 만약 X가 해당 수로 나눠진다면
        if x % i == 0:
            # 소수가 아님
            return False
    # 소수임
    return True

print(is_prime_number(7))