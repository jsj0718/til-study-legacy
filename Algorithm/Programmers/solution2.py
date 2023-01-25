def solution(arr1, arr2):
    answer = -1
    cnt = 0
    arr_list = []
    for i in arr1:
        for j in arr2:
            if (i[0] != ")" and j[-1] != "("):
                new_arr = i + j
                if (new_arr.count("(") == new_arr.count(")")) and (new_arr[:len(new_arr)].count("(") >= new_arr[len(new_arr):].count("(")):
                    cnt += 1
                    arr_list.append(new_arr)
    answer = cnt
    return answer

# 예시 1
arr1 = ["()", "(()", ")()", "()"]
arr2 = [")()", "()", "(()"]

print(solution(arr1, arr2))

# 예시 2
arr1 = ["()", "(()", "(", "(())"]
arr2 = [")()", "()", "(())", ")()"]

print(solution(arr1, arr2))