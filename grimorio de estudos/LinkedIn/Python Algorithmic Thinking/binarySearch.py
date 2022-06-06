import random


def binary_search(data, target):
    lowPointer = 0
    highPointer = len(data) - 1
    
    while True:
        ''' if data[lowPointer] == target:
            return lowPointer
        elif data[highPointer] == target:
            return highPointer
         '''
        
        midPoint = lowPointer + highPointer // 2

        if data[midPoint] == target:
            return midPoint
        elif data[midPoint] > target:
            highPointer = midPoint - 1
        else:
            lowPointer = midPoint + 1
        
        if lowPointer == highPointer:
            return -1
            



n = 10
max_val = 100
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
print("Data:", data)
target = int(input("Enter target value: "))
target_pos = binary_search(data, target)
if target_pos == -1:
    print("Your target value is not in the list.")
else:
    print("You target value has been found at index", target_pos)