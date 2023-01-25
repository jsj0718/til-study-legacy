# a * b 에서 b의 각 자리수와 곱한 값과 a*b의 값을 구하는 문제

a = int(input())
b = list(map(int, list(input()))) # 숫자 쪼개기 e.x) 487 -> [4,8,7]

print(a*b[2])
print(a*b[1])
print(a*b[0])
print(a*int(''.join(list(map(str,b))))) # 숫자 리스트 하나로 합치기 (join 함수 이용)
# 숫자를 map함수로 모두 str형태인 list로 만들고, split()과 반대인 join()을 이용하여 하나로 합친 후 다시 int 함수로 숫자로 바꿔준다.



# 예시(위 내용 예시)

# a = [4, 8 ,7]
# s = ''.join(list(map(str, a)))
# print(int(s))