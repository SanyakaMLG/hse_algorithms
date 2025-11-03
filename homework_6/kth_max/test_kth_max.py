import pytest
import random

from kth_max.main import kth_max

@pytest.mark.parametrize("arr,k,expected", [
    ([5, 3, 7, 1, 9], 1, 9),
    ([5, 3, 7, 1, 9], 2, 7),
    ([5, 3, 7, 1, 9], 3, 5),
    ([5, 3, 7, 1, 9], 4, 3),
    ([5, 3, 7, 1, 9], 5, 1),
    ([1], 1, 1),
    ([2, 2, 2, 2], 1, 2),
    ([2, 2, 2, 2], 4, 2),
    ([1, 2, 3, 4, 5], 1, 5),
    ([1, 2, 3, 4, 5], 5, 1),
    ([5, 4, 3, 2, 1], 1, 5),
    ([5, 4, 3, 2, 1], 5, 1),
])
def test_kth_max_basic(arr, k, expected):
    assert kth_max(arr, k) == expected

@pytest.mark.parametrize("arr,k", [
    ([], 0),
    ([1], 0),
    ([1, 2], -1),
    ([1, 2], 3),
])
def test_kth_max_invalid(arr, k):
    assert kth_max(arr, k) is None

def test_large_input():
    arr = [i for i in range(10_000)]
    random.shuffle(arr)

    for k in range(1, 500, 19):
        assert kth_max(arr, k) == 10_000 - k
