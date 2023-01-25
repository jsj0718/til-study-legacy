# 문자열 재정렬

data = list(input())
data.sort()

string = ""
number = 0

for d in data:
    if d.isalpha():
        string += d
    else:
        number += int(d)

result = string + str(number)

print(result)