# Case 양식(a+b)

T = int(input())

for i in range(T):
    a, b = list(map(int, input().split()))
    print(f"Case #{i+1}: ", end='')
    print(a + b)