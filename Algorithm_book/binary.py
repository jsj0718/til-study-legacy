# def binary(n):
#     if n < 2:
#         print(n, end='')
#     else:
#         binary(n//2)
#         print(n%2, end='')
        
# n = int(input())
# binary(n)

n = int(input())
result = ''

def binary(n):
    global result
    if n < 2:
        result += str(n)
        return result
    else:
        binary(n//2)
        result += str(n%2)
        return result
        
binary(n)
print(result)