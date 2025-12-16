import pytest
from lcs.main import lcs

def check_subsequence(sub, full_text):
    it = iter(full_text)
    return all(char in it for char in sub)

    
@pytest.mark.parametrize("s1, s2, expected_len, possible_seqs", [
    ("abcde", "ace", 3, ["ace"]),
    ("abc", "abc", 3, ["abc"]),
    ("abc", "def", 0, [""]),
    ("agcat", "gac", 2, ["ga", "ac", "gc"]),
    ("banana", "atana", 4, ["aana"]),
    ("", "abc", 0, [""]),
    ("abc", "", 0, [""]),
    ("", "", 0, [""]),
])
def test_lcs_logic(s1, s2, expected_len, possible_seqs):
    length, seq = lcs(s1, s2)
    
    assert length == expected_len
    
    assert len(seq) == length
    
    assert check_subsequence(seq, s1)
    assert check_subsequence(seq, s2)

    if possible_seqs:
        assert seq in possible_seqs


def test_long_strings():
    s1 = "XMJYAUZ"
    s2 = "MZJAWXU"
    length, seq = lcs(s1, s2)
    assert length == 4
    assert seq == "MJAU"
