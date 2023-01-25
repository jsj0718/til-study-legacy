def solution(grades, weights, threshold):
    answer = 0
    # 총 점수 정의 (모든 성적 가중치 * 고유 가중치의 합)
    score = 0
    # 성적 리스트 정의
    grades_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
    # 성적 가중치 정의
    grades_weight = [10, 9, 8, 7, 6, 5, 4, 3, 0]
    # 성적 개수만큼 반복
    for i in range(len(grades)):
        # 성적 리스트에서 성적을 통해 인덱스를 구하고, 이를 통해 성적 가중치를 구한 뒤 고유 가중치를 곱함
        score += grades_weight[grades_list.index(grades[i])] * weights[i]
    # 답은 총 점수 - 졸업 기준
    answer = score - threshold     
    return answer