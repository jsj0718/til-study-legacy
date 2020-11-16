def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]
    p = list(range(1, n+1)) + list(range(n-1, 0, -1))
    cnt = -2
    b = -1
    c = True
    for d in p:
        for i in range(d):
            cnt += 2
            if b == 1:
                if c:
                    answer[i][d-1-i] = cnt
                else:
                    answer[n - d + i][n - 1 - i] = cnt
            elif b == -1:
                if c:
                    answer[d-1-i][i] = cnt
                else:
                    answer[n - 1 - i][n - d + i] = cnt
        cnt -= 1
        b *= -1
        if d == n:
            c = False

    if horizontal == True:
        return answer
    else:
        new_answer = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_answer[j][i] = answer[i][j]
        return new_answer