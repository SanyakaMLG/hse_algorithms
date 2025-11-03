import pytest
from iterative_sort.quicksort import quicksort
from iterative_sort.mergesort import mergesort

@pytest.mark.parametrize("input_arr,expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1], [1, 1, 2, 2]),
    ([0, -1, 5, 3, -2], [-2, -1, 0, 3, 5]),
    ([3, 3, 3], [3, 3, 3]),
])
def test_quicksort(input_arr, expected):
    assert quicksort(input_arr) == expected

@pytest.mark.parametrize("input_arr,expected", [
    ([], []),
    ([1], [1]),
    ([2, 1], [1, 2]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1], [1, 1, 2, 2]),
    ([0, -1, 5, 3, -2], [-2, -1, 0, 3, 5]),
    ([3, 3, 3], [3, 3, 3]),
])
def test_mergesort(input_arr, expected):
    assert mergesort(input_arr) == expected
