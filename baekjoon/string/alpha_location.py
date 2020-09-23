# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.


# string = list(input())
# alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # 원본
# alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # 바꿀 리스트

# for s in string:
#     if s in alpha:
#         alpha_list[alpha.index(s)] = string.index(s)
    
# for a in alpha_list:
#     if a in alpha:
#         alpha_list[alpha_list.index(a)] = -1
        
# for answer in alpha_list:
#     print(answer, end=' ')

string = list(input())
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # 원본
alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # 바꿀 리스트

for a in alpha:
    if a in string:
        alpha_list[alpha_list.index(a)] = string.index(a)
    else:
        alpha_list[alpha_list.index(a)] = -1

for answer in alpha_list:
    print(answer, end=' ')