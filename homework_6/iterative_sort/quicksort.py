def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    low, high = 0, len(arr) - 1
    stack = [(low, high)]

    while stack:
        l, h = stack.pop()
        if l < h:
            pivot_idx = partition(arr, l, h)
            stack.append((l, pivot_idx - 1))
            stack.append((pivot_idx + 1, h))

    return arr