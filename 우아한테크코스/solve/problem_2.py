def solution(s, op):
    answer = []

    for i in range(len(s)-1):
        # 사칙 연산이 "+"일 경우
        if op == "+":
            # 슬라이싱 이용 후 answer 리스트에 추가
            answer.append(int(s[:i+1]) + int(s[i+1:]))
        # 사칙 연산이 "-"일 경우
        if op == "-":
            # 슬라이싱 이용 후 answer 리스트에 추가
            answer.append(int(s[:i+1]) - int(s[i+1:]))
        # 사칙 연산이 "*"일 경우
        if op == "*":
            # 슬라이싱 이용 후 answer 리스트에 추가
            answer.append(int(s[:i+1]) * int(s[i+1:]))    
    return answer