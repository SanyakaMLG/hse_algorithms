import pytest
from typing import Optional
from balanced_tree.main import Node, is_balanced


def empty_tree() -> None:
    return None

def single_node() -> Node:
    return Node(1)

def balanced_tree_3() -> Node:
    #     1
    #    / \
    #   2   3
    return Node(1, Node(2), Node(3))

def balanced_tree_7() -> Node:
    #       4
    #     /   \
    #    2     6
    #   / \   / \
    #  1   3 5   7
    return Node(
        4,
        Node(2, Node(1), Node(3)),
        Node(6, Node(5), Node(7))
    )

def unbalanced_left_deep() -> Node:
    #   1
    #  /
    # 2
    #/
    #3
    return Node(1, Node(2, Node(3)))

def unbalanced_right_deep() -> Node:
    # 1
    #  \
    #   2
    #    \
    #     3
    return Node(1, None, Node(2, None, Node(3)))

def unbalanced_in_subtree() -> Node:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    #  /         \
    # 6           7
    #              \
    #               8
    return Node(
        1,
        Node(2, Node(4, Node(6))),
        Node(3, None, Node(5, None, Node(7, None, Node(8))))
    )

def balanced_but_not_complete() -> Node:
    #       1
    #      / \
    #     2   3
    #    /   /
    #   4   5
    return Node(
        1,
        Node(2, Node(4)),
        Node(3, Node(5))
    )

def unbalanced_at_root_only() -> Node:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    #        /
    #       6
    return Node(
        1,
        Node(2),
        Node(3, Node(4), Node(5, Node(6)))
    )
    

def test_empty_tree():
    assert is_balanced(empty_tree()) is True

def test_single_node():
    assert is_balanced(single_node()) is True

def test_balanced_3_nodes():
    assert is_balanced(balanced_tree_3()) is True

def test_balanced_7_nodes():
    assert is_balanced(balanced_tree_7()) is True

def test_balanced_not_complete():
    assert is_balanced(balanced_but_not_complete()) is True

def test_unbalanced_left_deep():
    assert is_balanced(unbalanced_left_deep()) is False

def test_unbalanced_right_deep():
    assert is_balanced(unbalanced_right_deep()) is False

def test_unbalanced_in_subtree():
    assert is_balanced(unbalanced_in_subtree()) is False

def test_unbalanced_at_root_only():
    assert is_balanced(unbalanced_at_root_only()) is False

def test_large_balanced_tree():
    #           8
    #         /   \
    #        4     12
    #       / \   /  \
    #      2   6 10  14
    #     / \ / \ / \ / \
    #    1 3 5 7 9 11 13 15
    def build_perfect_tree(vals, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(vals[mid])
        node.left = build_perfect_tree(vals, start, mid - 1)
        node.right = build_perfect_tree(vals, mid + 1, end)
        return node

    vals = list(range(1, 16))
    root = build_perfect_tree(vals, 0, len(vals) - 1)
    assert is_balanced(root) is True

def test_one_node_with_one_child():
    #   1
    #  /
    # 2
    root = Node(1, Node(2))
    assert is_balanced(root) is True

def test_one_node_with_two_children_one_deep():
    #     1
    #    / \
    #   2   3
    #      /
    #     4
    root = Node(1, Node(2), Node(3, Node(4)))
    assert is_balanced(root) is True

def test_one_node_with_two_children_two_deep_right():
    #     1
    #    / \
    #   2   3
    #        \
    #         4
    #          \
    #           5
    root = Node(1, Node(2), Node(3, None, Node(4, None, Node(5))))
    assert is_balanced(root) is False
