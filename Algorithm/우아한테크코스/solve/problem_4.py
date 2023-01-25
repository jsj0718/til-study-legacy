def solution(n, board):
    answer = 0
    row = col = 0
    for num in range(1, n ** 2 + 1):
        for i in range(n):
            for j in range(n):
                if num == board[i][j]:
                    if row != i:
                        d = abs(row - i)
                        if d <= n//2:
                            answer += d
                        else:
                            answer += n - d
                        row = i
                    if col != j:
                        d = abs(col - j)
                        if d <= n//2:
                            answer += d
                        else:
                            answer += n - d
                        col = j
                    answer += 1
                    break
    return answer