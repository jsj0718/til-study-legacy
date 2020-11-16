T = int(input())

for tc in range(T):
    s = list(input())
    first_list = ['0'] * len(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] != first_list[i]:
            for j in range(len(s)-i):
                first_list[i+j] = s[i]
            cnt += 1
    print("#{:d}".format(tc+1), cnt)