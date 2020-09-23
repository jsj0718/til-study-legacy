# 10개의 숫자가 주어지고, 42로 나눴을 때 나머지가 다른 것들의 개수를 구하는 문제

num_list = []
for i in range(10):
    num = int(input()) % 42
    num_list.append(num)

num_list = set(num_list)
num_list = list(num_list)
print(len(num_list))