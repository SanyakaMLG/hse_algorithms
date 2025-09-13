import pytest
from .main import is_palindrome


def test_palindrome_single_digit():
    assert is_palindrome(1)
    assert is_palindrome(7)
    assert is_palindrome(9)


def test_palindrome_even_digits():
    assert is_palindrome(1221)
    assert is_palindrome(3443)
    assert is_palindrome(1001)


def test_palindrome_odd_digits():
    assert is_palindrome(121)
    assert is_palindrome(12321)
    assert is_palindrome(98789)


def test_not_palindrome():
    assert not is_palindrome(12)
    assert not is_palindrome(123)
    assert not is_palindrome(123456)


def test_large_palindrome():
    num = int("1" + "0" * 1000 + "1")
    assert is_palindrome(num)


def test_large_not_palindrome():
    num = int("1" + "0" * 1000 + "2")
    assert not is_palindrome(num)


def test_large_not_palindrome2():
    num = int("1" + "0" * 400 + "2" + "0" * 600 + "1")
    assert not is_palindrome(num)


def test_negative_number_raises():
    with pytest.raises(ValueError, match="must be a positive integer"):
        is_palindrome(-121)


def test_zero():
    assert is_palindrome(0)
