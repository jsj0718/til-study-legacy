# 사전은 {key : value} 형식
cabinet = {3:"유재석", 100:"박명수"}

# 방법 1 : []사용
print(cabinet[3]) # 유재석, dictionary[key] = value
print(cabinet[100])

# 방법 2 : get() 사용
print(cabinet.get(3))
print(cabinet.get(100))

# print(cabinet[5]) # 해당 key값 없을 시, Error 발생
print(cabinet.get(5)) # 해당 key값 없을 시, None 출력
print(cabinet.get(5, "사용 가능")) # none 대신 "사용 가능"을 출력(key값이 없을 때 어떻게 출력할 것인지 설정 가능)

# key가 dictionary 안에 있는지 확인
print(3 in cabinet) # True, key in dictionary 형식
print(5 in cabinet) # False

cabinet1 = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet1["A-3"])
print(cabinet1["B-100"])

# 새 손님 (새 요소 추가)
cabinet1["C-20"] = "조세호" # dictionary[key] = value로 새로운 key에 value 대입 가능
cabinet1["A-3"] = "김종국" # 이미 key가 있으면 value가 update
print(cabinet1)

# 간 손님 (요소 제거)
del cabinet1["B-100"] # del dict[key] 형식
print(cabinet1)

# key만 출력
print(cabinet1.keys()) # 리스트 형태

# value만 출력
print(cabinet1.values()) # 리스트 형태

# key, value 형식으로 출력
print(cabinet1.items()) # 리스트 형태
print(cabinet1) # 사전 형태

# 목욕탕 폐점 (모든 요소 제거)
cabinet1.clear()
print(cabinet1)