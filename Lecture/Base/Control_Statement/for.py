# for문

# # 예시 1
# for i in range(1, 21): # range(시작번호, 끝번호(포함X))
#     print("대기번호 : {0}".format(i))

# 예시 2
# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}님, 커피 준비되었습니다.".format(customer))


# 한줄 for문
# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101,102,103,104
# students = [1,2,3,4]
# students = [i+100 for i in students] # [조건 for i in 범위]
# print(students)

# 학생 이름을 길이로 변환

# students = ["Iron man", "Thor", "I am groot"]
# students_length = [len(student) for student in students]
# print(students_length)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students_upper = [student.upper() for student in students]
print(students_upper)