import time
start_time = time.time()

def solution(n, battery):
    answer = 0
    # Case1 : 하나의 견적 단위로 n개 이상 구매 시 가격 리스트 선언
    price_list1 = []
    # Case2 : 한 가지 이상의 견적 단위로 n개 이상 구매 시 가격 리스트 선언
    price_list2 = []
    # Case1과 Case2의 최소 금액
    price1 = price2 = 0

    # Case1

    # battery의 견적 단위 item 꺼내기
    for item_count, item_price in battery:
        # 견적 단위 item의 수량이 n보다 큰 경우
        if item_count >= n:
            # 그대로 견적 단위 item의 가격 추가
            price_list1.append(item_price)
        # 그 외
        else:
            # n개 수량 * (견적 단위 가격 / 견적 단위 수량) 추가 (단, n개 이상이므로 올림 필요)
            import math
            price_list1.append(math.ceil(n / item_count) * item_price)
    
    # Case1의 최소 금액 
    price1 = min(price_list1)

    # Case2

    # n이 0보다 같거나 작아질 때까지 반복
    while n > 0:
        # battery의 견적 단위 item 꺼내기
        for item_count, item_price in battery:
            # n보다 크면 견적 단위 금액 추가
            if item_count >= n:
                price_list2.append(item_price)
            # 그 외
            else:
                # n // 견적 단위 수량 * 견적 단위 가격 (한 가지 이상의 종류이므로 n을 초과할 필요는 없다.)
                price_list2.append(n // item_count * item_price)
        
        # Case2 가격 리스트의 최소 금액 인덱스 선언
        idx = price_list2.index(min(price_list2))
        # n을 구매한만큼 빼기
        n -= battery[idx][0] * min(price_list2) // battery[idx][1]
        # Case2의 최소 금액을 n이 0보다 작거나 같을 때까지 더하기
        price2 += min(price_list2)
        # 반복이 끝날 때마다 Case2의 가격 리스트 초기화
        price_list2.clear()

    # 두 가격 중 최소 금액 선정
    answer = min(price1, price2)
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

end_time = time.time()
print(end_time - start_time)