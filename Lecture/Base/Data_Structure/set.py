# 집합 (set)
# 중복 X, 순서 무작위

my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}, 중복 허용 X

# 집합 선언 방법 2가지 (순서 무작위로 출력됨)
java = {"유재석", "김태호", "박명수"}
python = set(["유재석", "정형돈", "노홍철", "하하"])

# 교집합 (방법 2가지)
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python) # 김태호, 박명수
print(java.difference(python))

# 요소 추가
java.add("정형돈") # add는 자료 하나 추가
print(java)

# java.update("정대만", "이대만", "김대만") # update는 자료 여러 개 추가, 그러나 자료형을 하나하나 다 쪼개서 추가 (겹치면 삭제)
# print(java)

# 요소 제거
java.remove("김태호")
print(java)