from permutations.main import permutations
from itertools import permutations as itertools_permutations

def test_permutations_empty_list():
    nums = []
    expected = list(itertools_permutations(nums))
    result = permutations(nums)
    assert sorted(result) == sorted([list(p) for p in expected])

def test_permutations_single_element():
    nums = [42]
    expected = list(itertools_permutations(nums))
    result = permutations(nums)
    assert sorted(result) == sorted([list(p) for p in expected])

def test_permutations_multiple_elements():
    nums = [1, 2, 3]
    expected = list(itertools_permutations(nums))
    result = permutations(nums)
    assert sorted(result) == sorted([list(p) for p in expected])

def test_permutations_with_duplicates():
    nums = [1, 1, 2]
    expected = list(itertools_permutations(nums))
    result = permutations(nums)
    assert sorted(result) == sorted([list(p) for p in expected])

def test_permutations_large_input():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = list(itertools_permutations(nums))
    result = permutations(nums)
    assert sorted(result) == sorted([list(p) for p in expected])