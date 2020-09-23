# 대학생 점수 평균을 넘는 학생 비율 구하기

n = int(input())

for nc in range(n):
    universe = list(map(int, input().split()))
    students = universe[0]
    scores = universe[1:]
    average = sum(scores) / students
    average_up = []

    for score in scores:
        if score > average:
            average_up.append(score)
    
    rate = round((len(average_up) / len(scores))* 100, 3)
    print("{:.3f}".format(rate) + "%") # 소수 표시


