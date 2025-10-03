from anagrams.main import group_anagrams


def test_group_anagrams_example():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])


def test_group_anagrams_empty_input():
    assert group_anagrams([]) == []


def test_group_anagrams_single_word():
    assert group_anagrams(["hello"]) == [["hello"]]


def test_group_anagrams_all_anagrams():
    assert group_anagrams(["abc", "bca", "cab"]) == [["abc", "bca", "cab"]]


def test_group_anagrams_no_anagrams():
    result = group_anagrams(["abc", "def", "ghi"])
    expected = [["abc"], ["def"], ["ghi"]]
    assert sorted([sorted(g) for g in result]) == sorted([sorted(g) for g in expected])


def test_group_anagrams_with_duplicates():
    result = group_anagrams(["abc", "bca", "abc"])
    assert sorted([sorted(g) for g in result]) == [["abc", "abc", "bca"]]
