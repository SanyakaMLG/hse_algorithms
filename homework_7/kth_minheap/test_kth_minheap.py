import pytest
from kth_minheap.main import kth_minheap, kth_minheap_heapq


def test_kth_minheap():
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k) == 5

    arr = [1, 2, 3, 4, 5]
    k = 3
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k) == 3

    arr = [2, 2, 2, 2]
    k = 2
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k) == 2

    arr = [-1, -2, -3, -4]
    k = 2
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k) == -2

    arr = [10, 5, 8, 12, 3]
    k = 1
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k) == 12

    arr = [7, 6, 5, 4, 3, 2, 1]
    k = len(arr)
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k) == 1

    with pytest.raises(ValueError):
        kth_minheap([], 1)
    with pytest.raises(ValueError):
        kth_minheap([1, 2], 3)