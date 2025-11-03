import pytest
from recursive_sort.quicksort import quicksort, quicksort_inplace
from recursive_sort.mergesort import mergesort

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
    assert quicksort(input_arr)[0] == expected

def test_quicksort_does_not_modify_input():
    arr = [3, 2, 1]
    arr_copy = arr[:]
    quicksort(arr)
    assert arr == arr_copy

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
def test_quicksort_inplace(input_arr, expected):
    assert quicksort_inplace(input_arr)[0] == expected

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
    assert mergesort(input_arr)[0] == expected

def test_mergesort_does_not_modify_input():
    arr = [3, 2, 1]
    arr_copy = arr[:]
    mergesort(arr)
    assert arr == arr_copy