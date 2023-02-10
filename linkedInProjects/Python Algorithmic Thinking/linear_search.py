def linear_search(data, target):
    for x in range(0, (len(data)+1)):
        if data[x] == target:
            result = x
            return result
        else:
            result = -1
    return result



data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")