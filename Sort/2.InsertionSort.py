import random;

numbers = [random.randint(1,100) for _ in range(20)]

# Start at 1, since the first element (index 0) is already "sorted"
for i in range(1, len(numbers)):
    temp = numbers[i]  # The "new element" to sort
    j = i - 1          # Start checking against the sorted elements to the left
    
    # Check the element to the left of temp
    # If the element is greater than temp, swap numbers[j] -> numbers[j+1]
        # The first element rewritten = temp so no worries
    # Move the index to left  using j-=1
    # Repeat until number[j-1] > temp
    while j >= 0 and numbers[j] > temp:
        numbers[j+1] = numbers[j]
        j -= 1
        
    # If/When we find an index which is smaller on the left and bigger on the right,
    #   We got the right location, so write the temp to here.
    #   Note that everything was shifted to right before this to accomodate this
    numbers[j+1] = temp
    
    print(numbers)

"""
단계별 실행 결과 예시:
Initial (초기 상태): [84, 12, 59, 3, 47, 21]
Pass 1: [12, 84, 59, 3, 47, 21] (12 삽입 / Inserted 12)
Pass 2: [12, 59, 84, 3, 47, 21] (59 삽입 / Inserted 59)
Pass 3: [3, 12, 59, 84, 47, 21] (3 삽입  / Inserted 3)
Pass 4: [3, 12, 47, 59, 84, 21] (47 삽입 / Inserted 47)
Pass 5: [3, 12, 21, 47, 59, 84] (21 삽입 / Inserted 21) - Final Sorted
"""