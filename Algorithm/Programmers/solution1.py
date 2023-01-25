def mult(num):
    result = 1
    for i in str(num):
        result *= int(i)

    return result

def solution(num):
    answer = 0
    length = len(str(num))
    front_num = int(str(num)[:length//2])
    back_num = int(str(num)[length//2:])
    
    while mult(front_num) != mult(back_num):
        if length % 2 != 0:
            break
        back_num = back_num + 1
    
    num = int(str(front_num) + str(back_num))
    answer = num
    return answer


print(solution(235386))