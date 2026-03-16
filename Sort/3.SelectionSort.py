# Traver the entire list and find the smallest value
# Insert the smallest value at the head of the list
# Repeat at next index until the end

import random;

numbers = [random.randint(1,100) for _ in range(20)]

print(numbers)
for i in range(len(numbers)):
    # Current Index 
    smallest = numbers[i]
    smallestIndex = i
    
    # Temp
    temp = numbers[i]

    # Index Traverser
    currIndex = i+1 

    while currIndex < len(numbers):
        if(numbers[currIndex] < smallest):
            smallest = numbers[currIndex]
            smallestIndex = currIndex
        currIndex += 1
    numbers[i] = smallest
    numbers[smallestIndex] = temp
    print(numbers)
    
print(numbers)