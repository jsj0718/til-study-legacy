# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

n = int(input())
count = []
for nc in range(n):

    string = list(input()) # aabbbcca
    word_count = 0
    
    for i in range(len(string)-1): # 0~5
        if string[i] == string[i+1]: # s[0] == s[1] ~ s[5] == s[6] 비교
            string[i] = " "

    while " " in string:
        string.remove(" ")

    for s in string:
        if string.count(s) >= 2:
            word_count = 0
            break
        else:
            word_count = 1
    
    count.append(word_count)
print(sum(count))
