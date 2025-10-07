import pytest
from typing import Optional
from validate_bst.main import Node, validate_bst

def test_empty_tree():
    assert validate_bst(None) is True

def test_single_node():
    root = Node(42)
    assert validate_bst(root) is True

@pytest.mark.parametrize("tree_func, expected", [
    (lambda: _build_tree([5, 3, 7]), True),
    (lambda: _build_tree([5, 6, 7]), False),
    (lambda: _build_tree([5, 3, 4]), False),
    (lambda: _build_deep_invalid_left(), False),
    (lambda: _build_deep_invalid_right(), False),
    (lambda: _build_with_duplicates(), False),
    (lambda: _build_negative_valid(), True),
    (lambda: _build_negative_invalid(), False),
    (lambda: _build_degenerate_valid(), True),
    (lambda: _build_degenerate_invalid(), False),
    (lambda: _build_large_valid(), True),
    (lambda: _build_equal_to_root_in_right(), False),
])
def test_validate_bst_parametrized(tree_func, expected):
    root = tree_func()
    assert validate_bst(root) is expected


def _build_tree(vals):
    root = Node(vals[0])
    if vals[1] is not None:
        root.left = Node(vals[1])
    if vals[2] is not None:
        root.right = Node(vals[2])
    return root

def _build_deep_invalid_left():
    #       10
    #      /  \
    #     5    15
    #    / \
    #   2   11
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(11)
    return root

def _build_deep_invalid_right():
    #       10
    #      /  \
    #     5    15
    #         /  \
    #        6    20
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(6)
    root.right.right = Node(20)
    return root

def _build_with_duplicates():
    #     5
    #    / \
    #   5   5
    root = Node(5)
    root.left = Node(5)
    root.right = Node(5)
    return root

def _build_negative_valid():
    #     -5
    #    /  \
    #  -10  -3
    root = Node(-5)
    root.left = Node(-10)
    root.right = Node(-3)
    return root

def _build_negative_invalid():
    #     -5
    #    /  \
    #  -3   -10
    root = Node(-5)
    root.left = Node(-3)
    root.right = Node(-10)
    return root

def _build_degenerate_valid():
    # 5 -> 4 -> 3 -> 2 -> 1 (только левые)
    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.left.left = Node(2)
    root.left.left.left.left = Node(1)
    return root

def _build_degenerate_invalid():
    # 5
    #  \
    #   10
    #  /
    # 4
    root = Node(5)
    root.right = Node(10)
    root.right.left = Node(4)
    return root

def _build_large_valid():
    #         10
    #       /    \
    #      5      15
    #     / \    /  \
    #    3   7  12   20
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)
    return root

def _build_equal_to_root_in_right():
    #     10
    #    /  \
    #   5    15
    #       /
    #      10
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(10)
    return root