memo = {}

def solve(remain, sitted):
    key = (remain, sitted)
    
    # 종료 조건
    if key in memo:
        return memo[key]
    if remain < 0:
        return 0
    if remain == 0:
        return 1
    
    # 재귀 처리
    count = 0
    for i in range(sitted, 11):
        count += solve(remain-i, i)

    # 메모화 처리
    memo[key] = count
    
    # 종료
    return count

print(solve(100,2))

    