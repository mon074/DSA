arr=[8, 3, 5, 2]

n = len(arr)

for key in range(1, n):
    key_value = arr[key]      # store the value to be inserted
    i = key - 1

    # shift elements that are greater than key_value
    while i >= 0 and arr[i] > key_value:
        arr[i + 1] = arr[i]
        i -= 1

    # insert key_value at correct position
    arr[i + 1] = key_value
print(arr)

