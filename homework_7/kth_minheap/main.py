import heapq


def kth_minheap_heapq(arr: list, k: int):
    if k <= 0 or k > len(arr):
        raise ValueError("k is out of bounds")

    h = []
    for num in arr:
        if len(h) == k and num > h[0]:
            heapq.heapreplace(h, num)
        elif len(h) < k:
            heapq.heappush(h, num)

    return h[0]


def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] >= heap[parent]:
            break
        heap[i], heap[parent] = heap[parent], heap[i]
        i = parent


def sift_down(heap, i):
    n = len(heap)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest


def heap_push(heap, value):
    heap.append(value)
    sift_up(heap, len(heap) - 1)


def heap_replace(heap, value):
    if not heap:
        return
    heap[0] = value
    sift_down(heap, 0)


def kth_minheap(arr: list, k: int):
    if k <= 0 or k > len(arr):
        raise ValueError("k is out of bounds")

    heap = []
    for num in arr:
        if len(heap) < k:
            heap_push(heap, num)
        else:
            if num > heap[0]:
                heap_replace(heap, num)
    return heap[0]