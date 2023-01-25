# 광원에서 금을 최대로 캘 수 있는 경우를 구하는 문제

for tc in range(int(input())):
    # 정수 n, m 입력
    n, m = map(int, input().split())
    # n * m 배열을 리스트 형태로 입력
    array = list(map(int, input().split()))

    # DP 테이블 초기화
    dp = []
    index = 0
    # 인덱스 값을 이용해서 리스트 형태인 array를 2차원 배열 형태로 변환
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            if i == n - 1: left_down = 0
            else: left_down = dp[i+1][j-1]

            # 왼쪽에서 오는 경우
            left = dp[i][j-1]

            # dp[i][j]의 값과 왼쪽에서 오는 경우의 최대값을 더한다.
            dp[i][j] = dp[i][j] + max(left, left_up, left_down)
        
    result = 0
    for i in range(n):
        # m번째 열에서의 최대값을 구하는 과정
        result = max(result, dp[i][m-1])
    print(result)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
19
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
16
"""