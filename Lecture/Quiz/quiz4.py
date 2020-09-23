# 20명의 지원자 중 1명의 치킨 당첨자, 3명의 피자 당첨자를 뽑는 프로그램을 작성하시오.

# 내 풀이

# from random import *

# student = []
# for i in range(1,21):
#     student.append(i)

# shuffle(student) # shuffle() : 무작위로 섞음. return값이 없음. 
# student_choice = sample(student,5) # sample(요소들, 개수) : 요소들을 무작위로 섞은 후 원하는 개수만큼 뽑아 리스트로 만듦.
# chicken = student_choice[0] # 새로 만들어진 랜덤 리스트에서 0번째 인덱스에 해당하는 값
# pizza = student_choice[1:4] # 새로 만들어진 랜덤 리스트에서 1~3번째 인덱스에 해당하는 값
# print("""\
#  -- 당첨자 발표 --
# 치킨 당첨자 : {0}
# 커피 당첨자 : {1}
#  -- 축하합니다. --\
# """.format(chicken, pizza))

# 해설
from random import *
users = range(1,21) # range 함수를 통해 1~20까지 정수들을 출력 가능
users = list(users) # range Type을 list Type으로 변경

shuffle(users) # 무작위로 섞음
winners = sample(users, 4) # 무작위로 한 번 더 섞은 후에 4명 선발

print("""\
 -- 당첨자 발표 --
치킨 당첨자 : {0}
커피 당첨자 : {1}
 -- 축하합니다. --\
""".format(users[0], users[1:4])) # 인덱스를 통해 값이 겹치지 않게 함