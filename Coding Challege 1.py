def find_min_diff_index(arr):
    mean = sum(arr) / len(arr)
    min_diff = float('inf')
    min_index = -1

    for i in range(len(arr)):
        diff = abs(arr[i] - mean)
        if diff < min_diff:
            min_diff = diff
            min_index = i
        elif diff == min_diff and i < min_index:
            min_index = i

    return min_index

# Example usage
n = 4
arr = [1, 2, 3, 4]
print(find_min_diff_index(arr))  # Output: 1