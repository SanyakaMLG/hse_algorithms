import pytest
from typing import List
from traversal.main import BST


def build_bst_from_list(values: List[int]) -> BST:
    bst = BST()
    for v in values:
        bst.insert(v)
    return bst


@pytest.fixture
def empty_bst():
    return BST()


@pytest.fixture
def single_node_bst():
    bst = BST()
    bst.insert(42)
    return bst

#       5
#      / \
#     3   7
@pytest.fixture
def simple_bst():
    return build_bst_from_list([5, 3, 7])

#         4
#       /   \
#      2     6
#     / \   / \
#    1   3 5   7
@pytest.fixture
def full_bst():
    return build_bst_from_list([4, 2, 6, 1, 3, 5, 7])

# 1 -> 2 -> 3 -> 4
@pytest.fixture
def degenerate_right_bst():
    return build_bst_from_list([1, 2, 3, 4])

# 4 -> 3 -> 2 -> 1
@pytest.fixture
def degenerate_left_bst():
    return build_bst_from_list([4, 3, 2, 1])


def test_empty_bst_traversals(empty_bst):
    assert empty_bst.in_order() == []
    assert empty_bst.pre_order() == []
    assert empty_bst.post_order() == []
    assert empty_bst.reverse_in_order() == []
    assert empty_bst.reverse_pre_order() == []
    assert empty_bst.reverse_post_order() == []


def test_single_node_bst_traversals(single_node_bst):
    assert single_node_bst.in_order() == [42]
    assert single_node_bst.pre_order() == [42]
    assert single_node_bst.post_order() == [42]
    assert single_node_bst.reverse_in_order() == [42]
    assert single_node_bst.reverse_pre_order() == [42]
    assert single_node_bst.reverse_post_order() == [42]


def test_simple_bst_traversals(simple_bst):
    #     5
    #    / \
    #   3   7

    assert simple_bst.in_order() == [3, 5, 7]
    assert simple_bst.pre_order() == [5, 3, 7]
    assert simple_bst.post_order() == [3, 7, 5]

    assert simple_bst.reverse_in_order() == [7, 5, 3]
    assert simple_bst.reverse_pre_order() == [5, 7, 3]
    assert simple_bst.reverse_post_order() == [7, 3, 5]


def test_full_bst_traversals(full_bst):
    #         4
    #       /   \
    #      2     6
    #     / \   / \
    #    1   3 5   7

    assert full_bst.in_order() == [1, 2, 3, 4, 5, 6, 7]
    assert full_bst.pre_order() == [4, 2, 1, 3, 6, 5, 7]
    assert full_bst.post_order() == [1, 3, 2, 5, 7, 6, 4]

    assert full_bst.reverse_in_order() == [7, 6, 5, 4, 3, 2, 1]
    assert full_bst.reverse_pre_order() == [4, 6, 7, 5, 2, 3, 1]
    assert full_bst.reverse_post_order() == [7, 5, 6, 3, 1, 2, 4]
    

def test_degenerate_right_bst(degenerate_right_bst):
    # 1 -> 2 -> 3 -> 4 (все вправо)

    assert degenerate_right_bst.in_order() == [1, 2, 3, 4]
    assert degenerate_right_bst.pre_order() == [1, 2, 3, 4]
    assert degenerate_right_bst.post_order() == [4, 3, 2, 1]

    assert degenerate_right_bst.reverse_in_order() == [4, 3, 2, 1]
    assert degenerate_right_bst.reverse_pre_order() == [1, 2, 3, 4]
    assert degenerate_right_bst.reverse_post_order() == [4, 3, 2, 1]


def test_degenerate_left_bst(degenerate_left_bst):
    # 4 -> 3 -> 2 -> 1 (все влево)

    assert degenerate_left_bst.in_order() == [1, 2, 3, 4]
    assert degenerate_left_bst.pre_order() == [4, 3, 2, 1]
    assert degenerate_left_bst.post_order() == [1, 2, 3, 4]

    assert degenerate_left_bst.reverse_in_order() == [4, 3, 2, 1]
    assert degenerate_left_bst.reverse_pre_order() == [4, 3, 2, 1]
    assert degenerate_left_bst.reverse_post_order() == [1, 2, 3, 4]


def test_reverse_in_order_is_reversed_in_order(full_bst, simple_bst, degenerate_right_bst):
    for bst in [full_bst, simple_bst, degenerate_right_bst]:
        assert bst.reverse_in_order() == list(reversed(bst.in_order()))


def test_duplicates_ignored():
    bst = BST()
    bst.insert(5)
    bst.insert(5)
    bst.insert(5)
    assert bst.in_order() == [5]
    assert bst.pre_order() == [5]
    assert bst.post_order() == [5]