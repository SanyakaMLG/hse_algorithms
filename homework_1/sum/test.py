import random
import pytest
from .main import even_sum


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),  # empty list
        ([2, 4, 6], 12),  # all even, sum already even
        ([1], 0),  # single odd, removing it
        ([2], 2),  # single even
        ([1, 2, 3], 6),  # sum already even
        ([1, 2, 6], 8),  # sum odd, remove smallest odd (1)
        ([7, 9, 3], 16),  # sum odd, remove smallest odd (3)
        ([10, 21, 32, 43], 106),  # sum odd, remove smallest odd (21)
        ([5, 5, 5], 10),  # sum odd (15), remove smallest odd (5)
        ([1000001, 1000003], 2000004),  # large numbers
    ]
)
def test_even_sum(nums, expected):
    assert even_sum(nums) == expected


def test_large_input():
    nums = [random.randint(1, 10000) for _ in range(10000)]
    result = even_sum(nums)
    assert result % 2 == 0
    assert result <= sum(nums)
