import pytest
from stack_vs_queue.my_stack import Stack


def test_empty_stack():
    stack = Stack()
    assert stack.empty() is True


def test_push_and_peek():
    stack = Stack()
    stack.push(42)
    assert stack.peek() == 42
    assert stack.empty() is False


def test_push_multiple_and_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3


def test_pop_single_element():
    stack = Stack()
    stack.push(100)
    assert stack.pop() == 100
    assert stack.empty() is True


def test_pop_multiple_elements():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.empty() is True


def test_peek_on_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(IndexError, match="stack is empty"):
        stack.peek()


def test_pop_on_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(IndexError, match="stack is empty"):
        stack.pop()


def test_mixed_operations():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.pop() == 20
    stack.push(30)
    assert stack.peek() == 30
    assert stack.pop() == 30
    assert stack.pop() == 10
    assert stack.empty() is True