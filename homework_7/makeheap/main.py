def sift_up(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] >= arr[parent]:
            break
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent


def makeheap_n_log_n(arr):
    for i in range(1, len(arr)):
        sift_up(arr, i)
    return arr


def sift_down(arr, i):
    n = len(arr)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest == i:
            break
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        sift_down(arr, i)
    return arr
