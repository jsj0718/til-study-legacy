obj = [0] * 100

def solution(logs):
    answer = []
    table = [[0] * 100 for _ in range(10000)]
    for log in logs:
        p, q, s = map(int, log.split())
        table[p][q] = s
    for i in range(10000):
        if table[i] != obj and table[i] in table[:i] + table[i+1:]:
            answer.append('%04d' % i )
        else:
            answer.append("None")
    return answer