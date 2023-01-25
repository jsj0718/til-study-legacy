# numbers = [1,5,2,6,3,7,4]
# value_list = []

# for value in range(3):
#     value = int(input())
#     value_list.append(value)
# i, j, k = value_list

# i, j, k = list(map(int, input().split()))

# number_choice = numbers[i-1:j]
# number_choice.sort()
# print(number_choice[k-1])

# for a in range(1,4):
#     i, j, k = list(map(int,input().split()))
#     commands.append([i, j, k])
#     array_slice = array[i-1:j]
#     array_slice.sort()
#     answer.append(array_slice[k-1])

# def solution(array, commands):
#     array = []
#     commands = command(i, j, k)
#     answer = []
#     for a in range(1,4):
#         i, j, k = list(map(int,input().split()))
#         commands.append([i, j, k])
#         array_slice = array[i-1:j]
#         array_slice.sort()
#         answer.append(array_slice[k-1])
#     return answer

# answer = solution(array, commands)
# print(answer)

# 제출 양식 (함수로 제공, array와 commands를 대입하여 맞는지 확인)

def solution(array, commands):
    answer = []
    for commands_list in commands:
        i, j, k = commands_list
        array_slice = array[i-1:j]
        array_slice.sort()
        answer.append(array_slice[k-1])
    return answer