from recursive_sort.timer import timer


def partition(arr):
    mid = len(arr) // 2
    pivot = arr[mid]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return left, middle, right


@timer
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    left, middle, right = partition(arr)
    left = quicksort(left)
    right = quicksort(right)

    return left + middle + right


def partition_inplace(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


@timer
def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition_inplace(arr, low, high)
        quicksort_inplace(arr, low, pivot_idx - 1)
        quicksort_inplace(arr, pivot_idx + 1, high)

    return arr
