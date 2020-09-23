# 리스트 [] : 순서를 가지는 객체의 집합
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "김태호"]
print(subway)

# 조세호는 몇 번째에 있는가?
print(subway.index("조세호")) # 1, 문자열과 똑같이 0부터 시작한다. index 함수도 동일하게 적용됨

# 하하 탑승
# print(subway.append("하하")) # none, return 값이 없기 때문!
subway.append("하하")
print(subway)

# 정형돈이 유재석과 조세호 사이에 탑승
# print(subway.insert(1, "정형돈")) # none, append와 동일하게 return값이 없기 때문!
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 꺼냄
print(subway.pop()) # 하하, 꺼내진 값을 출력
print(subway) # 꺼내진 이후 남아있는 값들의 리스트를 출력

# print(subway.pop()) # 김태호, 꺼내진 값을 출력
# print(subway) # 꺼내진 이후 남아있는 값들의 리스트를 출력

# print(subway.pop()) # 조세호, 꺼내진 값을 출력
# print(subway) # 꺼내진 이후 남아있는 값들의 리스트를 출력

# 동명이인이 몇 명인지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 2

# 오름차순, 내림차순 정렬 가능
num_list = [5,2,3,4,1]

# print(num_list.sort()) # none, return값 x
num_list.sort() # 오름차순
print(num_list)

# print(num_list.reverse()) # none, return값 x
num_list.reverse()
print(num_list) # 내림차순

# 모두 지우기
# print(num_list.clear()) # none, return값 x
num_list.clear()
print(num_list)

# 다양한 자료형 리스트
num_list = [1,2,3,4,5]
mix_list = ["정대만", 26, True]

# 리스트 확장
# print(num_list.extend(mix_list)) # none, return값 x
num_list.extend(mix_list)
print(num_list)