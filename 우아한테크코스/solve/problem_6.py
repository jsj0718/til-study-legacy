# # 진표 풀이
# import time
# start_time = time.time()

# obj = [-1] * 100

# def solution(logs):
#     answer = []
#     table = [[-1] * 100 for _ in range(10000)]
#     for log in logs:
#         p, q, s = map(int, log.split())
#         table[p][q] = s
#     for i in range(10000):
#         if table[i] != obj and table[i] in table[:i] + table[i+1:] and table[i].count(-1) <= 95:
#             answer.append('%04d' % i )
#     if answer == []: answer = ['None']
#     return answer

# # 예시 1
# # logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

# # 예시 2
# logs = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]

# # 예시 3
# # logs = ["1901 10 50", "1909 10 50"]

# print(solution(logs))

# end_time = time.time()
# print(end_time - start_time)







# 내 풀이
import time
start_time = time.time()

def solution(logs):
    answer = []
    # Dictionary = {수강 번호 : [[문제 번호, 받은 점수]], ...} 선언
    log_dictionary = {}
    # 수험번호를 담는 리스트 선언
    log_list = []
    # 수험번호가 다를 때 문제 번호, 받은 점수가 같은 경우를 세는 변수 선언
    count = 0

    # log 하나씩 꺼내기
    for log in logs:
        # "수험번호 문제번호 받은점수" 형식의 log를 리스트인 [수험번호, 문제번호, 받은점수] 형식으로 변경
        log = log.split()
        log_person, log_num, log_score = log[0], log[1], log[2]
        
        # 수험번호가 리스트에 없으면 추가
        if log_person not in log_list:
            log_list.append(log_person)
        # Key인 수험번호가 dictionary에 없는 경우
        if log_person not in log_dictionary:
            # 새로운 value 리스트를 넣어 dictionary에 추가
            log_dictionary[log_person] = [[log_num, log_score]]
        # Key인 수험번호가 dictionary에 있는 경우
        elif log_person in log_dictionary:
            # 기존 value 리스트에 추가
            log_dictionary[log_person] += [[log_num, log_score]]

    # dictionary의 key 꺼내기 (key1, key2)
    for m in range(len(log_list) - 1):
        for n in range(m + 1, len(log_list)):
            # 비교를 위해 수험번호 key1, key2 선언
            key1, key2 = log_list[m], log_list[n]
            # key1 길이만큼 반복
            for i in range(len(log_dictionary[key1])):
                # key2 길이만큼 반복
                for j in range(len(log_dictionary[key2])):
                    # 서로 다른 수험번호의 key1과 key2의 value가 같은 경우
                    if log_dictionary[key1][i] == log_dictionary[key2][j]:
                        count += 1
                    # 만약 count가 5개 이상인 경우
                    if count >= 5:
                        # answer에 수험번호인 key1과 key2가 없으면 추가하기
                        if key1 not in answer:
                            answer.append(key1)
                        if key2 not in answer:
                            answer.append(key2)
                        # count 0으로 초기화하고 진행하기
                        count = 0
                        break
            # key1과 key2 비교가 끝나면 count를 0으로 초기화
            count = 0

    # 만약 answer가 빈 경우 "None" 출력
    if not answer:
        answer = ["None"]
    return answer


# 예시 1
# logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]

# 예시 2
logs = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]

# 예시 3
# logs = ["1901 10 50", "1909 10 50"]

print(solution(logs))

end_time = time.time()
print(end_time - start_time)