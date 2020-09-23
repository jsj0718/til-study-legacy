# +, -, *, /
print(1+1) # 2
print(3-2) # 1
print(2*4) # 8
print(10/5) # 2, /은 float 형태

# **(제곱), %(나머지), //(몫)
print(2**3) # 8
print(10%3) # 1, %는 나머지
print(10//3) # 3, //는 몫

# 대소 비교
print(10>3) # True
print(10<3) # False
print(5>=5) # True
print(6<=6) # True

# 값 비교
print(3==3) # True, 값 비교(같으면 True)
print(3!=3) # False, 값 비교(다르면 True)
print(not(3==3)) # False
print(not(3!=3)) # True

# and(&), or(|)
print((3>0) and (6>3)) # True
print((3>0 & (6>3))) # True
print((3>0) or (6<3)) # True
print((3>0) | (6<3)) # True

print(5>4>3) # True
print(5>4>7) # False

# 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20, 괄호를 이용해서 우선 순위 변경 가능

number = 2 + 3 * 4
print(number) # 14
number = number + 2
print(number) # 16
number += 2
print(number) # 18
number -= 2
print(number) # 16
number *= 2
print(number) # 32
number /= 2
print(number) # 16.0 (float 형태)
number **= 2
print(number) # 256.0
number //= 2
print(number) # 128.0
number %= 10
print(number) # 8.0