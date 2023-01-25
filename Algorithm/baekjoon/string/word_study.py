# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

string = list(input().upper())
string_cnt = dict()
cnt_list = []

for s in string:
    if s not in string_cnt:
        string_cnt[s] = 1
    else:
        string_cnt[s] += 1

for key, value in string_cnt.items():
    max_value = max(string_cnt.values())
    if value == max_value:
        cnt_list.append(key)

if len(cnt_list) == 1:
    print(cnt_list[0])
else:
    print("?")

     
    