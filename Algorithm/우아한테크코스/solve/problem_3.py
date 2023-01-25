def solution(money, expected, actual):
    answer = -1
    # 초기 배팅금액 설정 (100원)
    betting = 100
    # 판 수만큼 반복
    for i in range(len(expected)):
        # 예측과 실제가 같은 경우
        if expected[i] == actual[i]:
            # 금액에 배팅금액 추가
            money += betting
            # 배팅금액 초기화
            betting = 100
        # 예측과 실제가 다른 경우
        else:
            # 금액에 배팅금액 빼기
            money -= betting
            # 금액이 현재 배팅금액의 2배 이상이면 다음 배팅금액을 현재의 2배로 설정
            if money >= (betting * 2):
                betting *= 2
            # 금액이 현재 배팅금액의 2배 이하면 다음 배팅금액을 전재산으로 설정
            elif money < (betting * 2):
                betting = money
            # 금액이 0원이면 0 return
            elif money == 0:
                return 0
    answer = money
    return answer

print(solution(1500,	['H', 'H', 'H', 'T', 'H'],	['T', 'T', 'T', 'H', 'H']))
