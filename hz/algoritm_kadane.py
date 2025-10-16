def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global


arr = list(map(int, input("Type number: ").split()))  # use space
print(f"max sum: {max_subarray_sum(arr)}")
