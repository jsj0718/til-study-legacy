# 튜플 : 내용 변경이나 추가 불가능, 그러나 리스트보다 속도가 빨라 고정된 값의 목록을 사용할 때 유용함

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # tuple은 add 지원 X

# name = "정대만"
# age = 26
# hobby = "코딩"
# print(name, age, hobby)

# 위처럼 변수 하나하나 선언하지 않고 아래처럼 선언하면 tuple 형식으로 저장됨
name, age, hobby = "정대만", 26, "코딩"
print(name) # "정대만"
print(age) # 26
print(hobby) # "코딩"