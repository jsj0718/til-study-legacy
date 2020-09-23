# 예시 (continue, break)

absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue # 건너뜀
    elif student in no_book:
        print("오늘 수업 종료, {0}은 교무실로 따라와".format(student))
        break # 반복문 중지
    print("{0}번 학생 책 읽어봐".format(student))


