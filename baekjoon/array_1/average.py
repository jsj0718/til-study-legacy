# 기존 점수를 기존 점수 / 최대값 점수 * 100로 변경 후 평균을 구하는 문제

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
score_change_list = []

for score in scores:
    score_change = score / max_score * 100
    score_change_list.append(score_change)

score_change_average = sum(score_change_list) / n
print(score_change_average)