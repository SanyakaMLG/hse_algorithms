import pytest
from avl.main import AVLTree


@pytest.fixture
def tree():
    return AVLTree()


def build_avl(tree, values):
    root = None
    for v in values:
        root = tree.insert(root, v)
    return root


def test_insert_balanced(tree):
    root = None
    for val in [10, 20, 30, 40, 50, 25]:
        root = tree.insert(root, val)

    assert tree.in_order(root) == [10, 20, 25, 30, 40, 50]

    def check_balance(node):
        if not node:
            return True
        balance = tree.get_balance(node)
        assert -1 <= balance <= 1
        return check_balance(node.left) and check_balance(node.right)

    assert check_balance(root)


def test_insert_duplicates(tree):
    root = build_avl(tree, [10, 10, 10])
    assert tree.in_order(root) == [10]


def test_delete_from_empty(tree):
    root = None
    result = tree.delete(root, 5)
    assert result is None


def test_delete_root_single_node(tree):
    root = tree.insert(None, 10)
    root = tree.delete(root, 10)
    assert root is None


def test_search_in_empty_tree(tree):
    assert tree.search(None, 10) is None


def test_balance_small_tree(tree):
    root = None
    root = tree.insert(root, 30)
    root = tree.insert(root, 20)
    root = tree.insert(root, 10)
    assert tree.in_order(root) == [10, 20, 30]
    assert abs(tree.get_balance(root)) <= 1


def test_insert_negative_numbers(tree):
    root = build_avl(tree, [-10, -20, -30, -5, -15])
    result = tree.in_order(root)
    assert result == sorted([-10, -20, -30, -5, -15])
    assert abs(tree.get_balance(root)) <= 1


def test_delete_all_elements(tree):
    values = [10, 20, 30, 40, 50, 25]
    root = build_avl(tree, values)
    for v in values:
        root = tree.delete(root, v)
    assert root is None


def test_in_order(tree):
    root = build_avl(tree, [10, 20, 5])
    assert tree.in_order(root) == [5, 10, 20]


def test_pre_order(tree):
    root = build_avl(tree, [10, 20, 5])
    result = tree.pre_order(root)
    assert set(result) == {10, 20, 5}
    assert len(result) == 3


def test_delete_node_with_two_children(tree):
    root = build_avl(tree, [20, 10, 30, 25, 40, 22])
    root = tree.delete(root, 30)
    assert tree.in_order(root) == [10, 20, 22, 25, 40]
    assert -1 <= tree.get_balance(root) <= 1


def test_min_value_node(tree):
    root = build_avl(tree, [50, 20, 70, 10, 30])
    min_node = tree.get_min_value_node(root)
    assert min_node.val == 10


def test_insert_sorted_sequence(tree):
    root = None
    for i in range(1, 11):
        root = tree.insert(root, i)
    assert abs(tree.get_balance(root)) <= 1
    assert tree.in_order(root) == list(range(1, 11))


def test_delete_non_existing_value(tree):
    root = build_avl(tree, [10, 20, 30])
    root = tree.delete(root, 999)  # Не должно ничего изменить
    assert tree.in_order(root) == [10, 20, 30]


def test_multiple_rotations(tree):
    root = None
    for v in [30, 10, 40, 5, 20, 35, 50, 25]:
        root = tree.insert(root, v)
    assert -1 <= tree.get_balance(root) <= 1
    assert tree.in_order(root) == sorted([30, 10, 40, 5, 20, 35, 50, 25])


def test_delete_root_with_children(tree):
    root = build_avl(tree, [10, 5, 15, 3, 7, 12, 20])
    root = tree.delete(root, 10)
    assert sorted(tree.in_order(root)) == [3, 5, 7, 12, 15, 20]
    assert -1 <= tree.get_balance(root) <= 1


def test_single_left_rotation(tree):
    root = None
    for v in [10, 20, 30]:
        root = tree.insert(root, v)
    assert root.val == 20  # После балансировки корень должен быть 20
    assert tree.in_order(root) == [10, 20, 30]


def test_single_right_rotation(tree):
    root = None
    for v in [30, 20, 10]:
        root = tree.insert(root, v)
    assert root.val == 20  # После балансировки корень должен быть 20
    assert tree.in_order(root) == [10, 20, 30]

