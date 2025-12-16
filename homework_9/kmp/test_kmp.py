import pytest
from kmp.main import kmp

@pytest.mark.parametrize("text, pattern, expected", [
    ("hello world", "hello", 0),
    ("hello world", "world", 6),
    ("hello world", "o w", 4),
    
    ("hello world", "python", -1),
    ("abc", "abcd", -1),
    
    ("", "", 0),
    ("abc", "", 0),
    ("", "a", -1),
    
    ("aaaaa", "aa", 0),
    ("ababa", "aba", 0),
    
    ("привет мир", "мир", 7),
    ("a\nb\tc", "\t", 3),
    
    ("abcdef", "def", 3),
    ("abcdef", "xyz", -1),
])
def test_kmp(text, pattern, expected):
    assert kmp(text, pattern) == expected
