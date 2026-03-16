# Traver the entire list and find the smallest and largest value
# Insert the smallest and largest value at the head and end of the list, respectively
# Repeat at next index until the end

import random;

numbers = [random.randint(1,100) for _ in range(21)]

print(numbers)
endOfList = len(numbers)-1
for i in range(len(numbers) //2 + 1):
    # Identifier for Smallest, Largest, and Index Traverser
    smallestIndex = i
    largestIndex = i
    currIndex = i

    #Finding the correct index for smallest and largest
    while currIndex <= endOfList:
        if(numbers[currIndex] < numbers[smallestIndex]):
            smallestIndex = currIndex
        if(numbers[currIndex] > numbers[largestIndex]):
            largestIndex = currIndex
        currIndex += 1

    # Replace the smallest 
    smallestTemp = numbers[i]
    numbers[i] = numbers[smallestIndex]
    numbers[smallestIndex] = smallestTemp

    # If the largestIndex == i, it was just replaced, so point to correct location
    if largestIndex == i:
        largestIndex = smallestIndex

    # Replace the largest
    largestTemp = numbers[endOfList]
    numbers[endOfList] = numbers[largestIndex]
    numbers[largestIndex] = largestTemp

    # Redirect EOL to new location
    endOfList -=1
    print(numbers)
    
print(numbers)