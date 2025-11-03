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


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    width = 1

    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]

            arr[i:min(i + 2 * width, len(arr))] = merge(left, right)

        width *= 2

    return arr