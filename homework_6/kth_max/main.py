def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_max(arr, k):
    if not 1 <= k <= len(arr):
        return None

    low, high = 0, len(arr) - 1
    target = len(arr) - k
    pivot_idx = -1

    while pivot_idx != target:
        pivot_idx = partition(arr, low, high)

        if pivot_idx < len(arr) - k:
            low = pivot_idx + 1
        else:
            high = pivot_idx - 1

    return arr[pivot_idx]
