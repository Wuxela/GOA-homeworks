def find_smallest_int(arr):
    if arr is None or len(arr) == 0:
        return None
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest