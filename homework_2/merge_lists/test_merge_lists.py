from merge_lists.main import merge_lists, merge_lists_dummy, Node
from typing import Optional


def create_linked_list(arr: list[int]) -> Optional[Node]:
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head


def test_merge_lists_both_empty():
    assert merge_lists(None, None) is None
    assert merge_lists_dummy(None, None) is None


def test_merge_lists_first_empty():
    l2 = create_linked_list([1, 2, 3])
    expected = create_linked_list([1, 2, 3])
    assert merge_lists(None, l2) == expected
    assert merge_lists_dummy(None, l2) == expected


def test_merge_lists_second_empty():
    l1 = create_linked_list([4, 5, 6])
    expected = create_linked_list([4, 5, 6])
    assert merge_lists(l1, None) == expected
    assert merge_lists_dummy(l1, None) == expected


def test_merge_lists_normal_case():
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    expected = create_linked_list([1, 2, 3, 4, 5, 6])
    assert merge_lists(l1, l2) == expected
    assert merge_lists_dummy(l1, l2) == expected


def test_merge_lists_one_list_smaller():
    l1 = create_linked_list([1, 2, 3])
    l2 = create_linked_list([4, 5, 6])
    expected = create_linked_list([1, 2, 3, 4, 5, 6])
    assert merge_lists(l1, l2) == expected
    assert merge_lists_dummy(l1, l2) == expected


def test_merge_lists_with_duplicates():
    l1 = create_linked_list([1, 1, 2])
    l2 = create_linked_list([1, 3, 3])
    expected = create_linked_list([1, 1, 1, 2, 3, 3])
    assert merge_lists(l1, l2) == expected
    assert merge_lists_dummy(l1, l2) == expected


def test_merge_lists_single_elements():
    l1 = create_linked_list([5])
    l2 = create_linked_list([3])
    expected = create_linked_list([3, 5])
    assert merge_lists(l1, l2) == expected
    assert merge_lists_dummy(l1, l2) == expected


def test_merge_lists_different_lengths():
    l1 = create_linked_list([1, 4, 6, 8])
    l2 = create_linked_list([2, 3, 5])
    expected = create_linked_list([1, 2, 3, 4, 5, 6, 8])
    assert merge_lists(l1, l2) == expected
    assert merge_lists_dummy(l1, l2) == expected


def test_merge_lists_identical_lists():
    l1 = create_linked_list([1, 2, 3])
    l2 = create_linked_list([1, 2, 3])
    expected = create_linked_list([1, 1, 2, 2, 3, 3])
    assert merge_lists(l1, l2) == expected
    assert merge_lists_dummy(l1, l2) == expected
