numbers = [42, 17, 8, 93, 25, 61, 4, 76]

print(numbers)
for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j] >= numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            print(numbers)
print(numbers)