from two_sum.main import two_sum

def test_two_sum_basic():
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)


def test_two_sum_equal_elements():
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)


def test_two_sum_first_and_last():
    assert two_sum([2, 7, 11, 15], 17) == (0, 3)


def test_two_sum_with_negative():
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)


def test_two_sum_zero_sum():
    assert two_sum([-3, 4, 3, 90], 0) == (0, 2)


def test_two_sum_two_elements():
    assert two_sum([3, 3], 6) == (0, 1)


def test_two_sum_large_numbers():
    assert two_sum([1000000000, 1000000000], 2000000000) == (0, 1)


def test_two_sum_one_element():
    assert two_sum([1], 1) is None


def test_two_sum_empty_arr():
    assert two_sum([], 0) is None