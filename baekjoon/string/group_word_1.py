# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

n = int(input())
count = 0

for nc in range(n):
    string = list(input()) # aabbbcca
    string_list = []
    word_count = 0
    str_len = len(string)

    for i in range(str_len):
        if str_len == 1:
            string_list.append(string[i])
        elif (i != str_len-1) and (string[i] != string[i+1]):
            string_list.append(string[i])
        elif (i == str_len-1) and (string[i] != string[i-1]):
            string_list.append(string[i])
    for s in string_list:
        if string_list.count(s) >= 2:
            word_count = 0
            break
        else:
            word_count = 1            
    count += word_count
print(count)
