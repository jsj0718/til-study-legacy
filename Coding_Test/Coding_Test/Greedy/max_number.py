# 문자열로 숫자가 주어졌을 때, 최대값 구하기

# 내 풀이(인덱스 활용)
# s = list(input())

# for i in range(len(s)-1):
#     if (int(s[0]) + int(s[1])) >= (int(s[0]) * int(s[1])):
#         s[0] = int(s[0]) + int(s[1])
#         s.remove(s[1])
#     else:
#         s[0] = int(s[0]) * int(s[1])
#         s.remove(s[1])
# print(int(s[0]))


# 문자열에 0, 1이 포함되면 +, 아니면 *

# 문자열로 이뤄진 숫자를 입력받기
data = input()
# result를 문자열의 첫 번째 숫자로 지정하기
result = int(data[0])

# 문자열을 차례대로 연산할 때 하나라도 0, 1이 포함되면 +, 그 외에는 *로 연산하기
for i in range(1, len(data)):
    num = int(data[i])
    # 0, 1을 ==로 비교하기보다 <=로 비교하는 것이 더 간결하다.
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)