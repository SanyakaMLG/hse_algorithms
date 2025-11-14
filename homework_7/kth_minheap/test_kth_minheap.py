import pytest
from kth_minheap.main import kth_minheap, kth_minheap_heapq


def test_kth_minheap_basic():
    assert kth_minheap([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_minheap([1, 2, 3, 4, 5], 3) == 3
    assert kth_minheap([2, 2, 2, 2], 2) == 2
    assert kth_minheap([-1, -2, -3, -4], 2) == -2
    assert kth_minheap([10, 5, 8, 12, 3], 1) == 12
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 7) == 1
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 6) == 2
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 5) == 3
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 4) == 4
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 3) == 5
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 2) == 6
    assert kth_minheap([7, 6, 5, 4, 3, 2, 1], 1) == 7

def test_kth_minheap_edge_cases():
    assert kth_minheap([5, 4, 3, 2, 1], 5) == 1
    assert kth_minheap([42], 1) == 42
    assert kth_minheap([0, 0, 0, 0], 3) == 0
    assert kth_minheap([-10, 0, 10], 2) == 0

def test_kth_minheap_invalid():
    with pytest.raises(ValueError):
        kth_minheap([], 1)
    with pytest.raises(ValueError):
        kth_minheap([1, 2], 3)
    with pytest.raises(ValueError):
        kth_minheap([1, 2, 3], 0)
    with pytest.raises(ValueError):
        kth_minheap([1, 2, 3], -1)


def test_kth_minheap_heapq_basic():
    assert kth_minheap_heapq([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_minheap_heapq([1, 2, 3, 4, 5], 3) == 3
    assert kth_minheap_heapq([2, 2, 2, 2], 2) == 2
    assert kth_minheap_heapq([-1, -2, -3, -4], 2) == -2
    assert kth_minheap_heapq([10, 5, 8, 12, 3], 1) == 12
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 7) == 1
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 6) == 2
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 5) == 3
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 4) == 4
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 3) == 5
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 2) == 6
    assert kth_minheap_heapq([7, 6, 5, 4, 3, 2, 1], 1) == 7

def test_kth_minheap_heapq_edge_cases():
    assert kth_minheap_heapq([5, 4, 3, 2, 1], 5) == 1
    assert kth_minheap_heapq([42], 1) == 42
    assert kth_minheap_heapq([0, 0, 0, 0], 3) == 0
    assert kth_minheap_heapq([-10, 0, 10], 2) == 0

def test_kth_minheap_heapq_invalid():
    with pytest.raises(ValueError):
        kth_minheap_heapq([], 1)
    with pytest.raises(ValueError):
        kth_minheap_heapq([1, 2], 3)
    with pytest.raises(ValueError):
        kth_minheap_heapq([1, 2, 3], 0)
    with pytest.raises(ValueError):
        kth_minheap_heapq([1, 2, 3], -1)


@pytest.mark.parametrize("arr, k", [
    ([3, 2, 1, 5, 6, 4], 2),
    ([1, 2, 3, 4, 5], 3),
    ([2, 2, 2, 2], 2),
    ([-1, -2, -3, -4], 2),
    ([10, 5, 8, 12, 3], 1),
    ([7, 6, 5, 4, 3, 2, 1], 7),
    ([5, 4, 3, 2, 1], 5),
    ([100], 1),
    ([0, 0, 0, 0], 3),
    ([-10, 0, 10], 2),
])
def test_kth_minheap_vs_heapq(arr, k):
    assert kth_minheap(arr, k) == kth_minheap_heapq(arr, k)