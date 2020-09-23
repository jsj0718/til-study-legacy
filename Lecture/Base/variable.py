animal = "강아지"
name = "연탄이"
age = 4
hobby = "공놀이"
is_adult = age >= 4

print("우리집 {0} 이름은 {1}입니다. 나이는 {2}살 이고요, 취미는 {3}입니다.".format(animal, name, age, hobby))
print("{0}는 어른일까요? {1}".format(name, is_adult))

# 주석 처리 Tip
# 1) #을 이용한다 (범위 선택 후 ctrl + /하면 주석 처리 가능)
# 2) ''' ~ ''' or """ ~ """를 이용한다