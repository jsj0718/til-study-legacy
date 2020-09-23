# 순차탐색

def search(li, begin, end, target):
    if begin > end:
        return -1
    elif li[begin] == target:
        return begin
    else:
        return search(li, begin+1, end, target)

li = [10, 29, 394, 293, 21, 23, 45]
print(search(li, 0, 10, 10)) # 1