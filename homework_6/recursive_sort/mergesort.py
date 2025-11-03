from recursive_sort.timer import timer


def merge(left, right):
    i, j = 0, 0

    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]


@timer
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    left = mergesort(arr[:n//2])
    right = mergesort(arr[n//2:])
    return merge(left, right)
