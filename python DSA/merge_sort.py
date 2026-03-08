def merge_sort(arr):
    # Base case: 0 or 1 element -> already sorted
    if len(arr) <= 1:
        return arr

    # 1) Split into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 2) Recursively sort both halves
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 3) Merge the two sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i, j = 0, 0  # pointers for left and right

    # Compare elements from both lists and build the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any leftovers (only one of these will run)
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))  # Output: [3, 9, 10, 27, 38, 43, 82]
