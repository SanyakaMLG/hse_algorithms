from validate.main import is_valid_seq


def test_valid_sequence_simple():
    assert is_valid_seq([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True


def test_invalid_sequence():
    assert is_valid_seq([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False


def test_empty_sequences():
    assert is_valid_seq([], []) is True


def test_single_element():
    assert is_valid_seq([1], [1]) is True


def test_single_element_invalid():
    assert is_valid_seq([1], [2]) is False


def test_pushed_and_popped_different_lengths():
    assert is_valid_seq([1, 2, 3], [1, 2]) is False
    assert is_valid_seq([1, 2], [1, 2, 3]) is False


def test_identical_order():
    assert is_valid_seq([1, 2, 3, 4], [1, 2, 3, 4]) is True


def test_reverse_order():
    assert is_valid_seq([1, 2, 3, 4], [4, 3, 2, 1]) is True


def test_complex_valid():
    assert is_valid_seq([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]) is True


def test_complex_invalid():
    assert is_valid_seq([1, 2, 3, 4, 5, 6], [2, 1, 4, 6, 3, 5]) is False


def test_duplicate_values():
    assert is_valid_seq([1, 2, 1], [1, 2, 1]) is True
    assert is_valid_seq([1, 2, 1], [1, 1, 2]) is True
    assert is_valid_seq([1, 2, 1], [2, 1, 1]) is True


def test_popped_element_not_in_pushed():
    assert is_valid_seq([1, 2, 3], [1, 4, 2]) is False