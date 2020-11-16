def game(number):
    count = 0
    for i in range(1, number + 1):
        for j in str(i):
            if j == "3" or j == "6" or j == "9":
                count += 1
    return count

print(game(33))