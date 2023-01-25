# 재귀 함수 메모화

dictionary = {
    1 : 1,
    2 : 1
}

def fibo(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibo(n-2) + fibo(n-1)
        dictionary[n] = output
        return output

print(dictionary, fibo(35))