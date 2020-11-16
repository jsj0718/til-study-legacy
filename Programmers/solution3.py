def solution(n, battery):
    answer = 0
    result = 0
    min_price = 99999999999999999999
    for item in battery:
        if item[0] >= n:
            if min_price > item[1]:
                min_price = item[1]
        else:
            import math
            if min_price > math.ceil(n / item[0]) * item[1]:
                min_price = math.ceil(n / item[0]) * item[1]

    while n > 0:
        price_list = []

        for item in battery:
            if item[0] >= n:
                price_list.append(item[1])
            else:
                price_list.append(n // item[0] * item[1])
        
        idx = price_list.index(min(price_list))
        result += min(price_list)
        n -= battery[idx][0] * (min(price_list) // battery[idx][1])
    
    answer = min(min_price, result)
    return answer

# 예시 1
n = 50
battery = [[10, 100000], [4, 35000], [1, 15000]]
print(solution(n, battery))

# 예시 2
n = 20
battery = [[6, 30000], [3, 18000], [4, 28000], [1, 9500]]
print(solution(n, battery))

# 예시 3
print(solution(11, [[2, 20000], [11, 115000]]))