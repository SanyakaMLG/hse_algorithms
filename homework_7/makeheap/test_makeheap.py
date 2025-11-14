from makeheap.main import makeheap_n_log_n, makeheap


def is_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True


def test_makeheap_n_log_n():
    arr = [3, 2, 1, 4, 5]
    result = makeheap_n_log_n(arr.copy())
    assert is_min_heap(result), "makeheap_n_log_n failed to create a valid min-heap"
    assert result[0] == 1, "Root of the heap is not the minimum element"

def test_makeheap():
    arr = [3, 2, 1, 4, 5]
    result = makeheap(arr.copy())
    assert is_min_heap(result), "makeheap failed to create a valid min-heap"
    assert result[0] == 1, "Root of the heap is not the minimum element"

def test_single_element():
    arr = [5]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert result1 == [5], "makeheap_n_log_n failed for single-element array"
    assert result2 == [5], "makeheap failed for single-element array"
    assert is_min_heap(result1), "makeheap_n_log_n failed for single-element array"
    assert is_min_heap(result2), "makeheap failed for single-element array"

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert is_min_heap(result1), "makeheap_n_log_n failed for sorted array"
    assert is_min_heap(result2), "makeheap failed for sorted array"
    assert result1[0] == 1, "Root of the heap is not the minimum element"
    assert result2[0] == 1, "Root of the heap is not the minimum element"

def test_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert is_min_heap(result1), "makeheap_n_log_n failed for reverse-sorted array"
    assert is_min_heap(result2), "makeheap failed for reverse-sorted array"
    assert result1[0] == 1, "Root of the heap is not the minimum element"
    assert result2[0] == 1, "Root of the heap is not the minimum element"

def test_random_array():
    import random
    arr = random.sample(range(100), 50)
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert is_min_heap(result1), "makeheap_n_log_n failed for random array"
    assert is_min_heap(result2), "makeheap failed for random array"
    assert result1[0] == min(arr), "Root of the heap is not the minimum element"
    assert result2[0] == min(arr), "Root of the heap is not the minimum element"

def test_empty_array():
    arr = []
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert result1 == [], "makeheap_n_log_n failed for empty array"
    assert result2 == [], "makeheap failed for empty array"
    assert is_min_heap(result1), "makeheap_n_log_n failed for empty array"
    assert is_min_heap(result2), "makeheap failed for empty array"

def test_two_elements():
    arr = [2, 1]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert result1 == [1, 2], "makeheap_n_log_n failed for two-element array"
    assert result2 == [1, 2], "makeheap failed for two-element array"
    assert is_min_heap(result1), "makeheap_n_log_n failed for two-element array"
    assert is_min_heap(result2), "makeheap failed for two-element array"
