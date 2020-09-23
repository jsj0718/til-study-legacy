# OX 문제(O가 연속되면 +1, +2, +3 ...)

# t = int(input()) # test 횟수
# count = 0 # 콤보 카운트
# idx = 0 # o,x 리스트의 index 번호 

# for tc in range(t):
#     n = list(input()) # o,x 리스트
#     while True:
#         if idx >= len(n): # 인덱스가 ox 리스트 개수와 동일해지거나 넘으면 break
#             break
#         elif n[idx] == "o":
#             count += 1

#         idx += 1
        
#     print(count)


n = int(input()) # test 횟수
count = 0 # 콤보 카운트

for nc in range(n): # 테스트 횟수만큼 반복
    t = list(input()) # o,x 리스트
    t_list = [] # 테스트 빈 리스트
    count_list = [] # 카운트 빈 리스트
    for i in range(len(t)-1): # 테스트 리스트 길이 -1만큼 반복(i+1과 비교해야하기 때문)
        if t[i] == "O" and t[i] == t[i+1]: # t[index] 가 "O"이고 앞과 동일하면
            t_list.append(t[i]) # 테스트 빈 리스트에 t값 대입
            count = len(t_list) # count는 테스트 리스트의 길이와 동일 (연속되는 o의 횟수, ooo면 count = 2)
            count_list.append(count) # 카운트 리스트에 count되는 횟수를 대입 (ooo면 카운트 리스트는 [1,2] 즉, 총합은 +3)
        else: # x면 테스트 리스트 삭제
            t_list.clear()
        
    print(t.count("O") + sum(count_list))