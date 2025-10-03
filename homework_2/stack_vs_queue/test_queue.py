import pytest
from stack_vs_queue.my_queue import Queue


def test_empty_queue():
    q = Queue()
    assert q.empty() is True


def test_push_single_element():
    q = Queue()
    q.push(42)
    assert q.empty() is False
    assert q.peek() == 42


def test_push_multiple_elements():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.peek() == 1


def test_pop_single_element():
    q = Queue()
    q.push(100)
    assert q.pop() == 100
    assert q.empty() is True


def test_pop_multiple_elements():
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)

    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.empty() is True


def test_peek_on_empty_queue_raises_exception():
    q = Queue()
    with pytest.raises(IndexError, match="queue is empty"):
        q.peek()


def test_pop_on_empty_queue_raises_exception():
    q = Queue()
    with pytest.raises(IndexError, match="queue is empty"):
        q.pop()


def test_mixed_operations():
    q = Queue()
    q.push(10)
    q.push(20)
    assert q.pop() == 10
    q.push(30)
    assert q.peek() == 20
    assert q.pop() == 20
    assert q.pop() == 30
    assert q.empty() is True


def test_push_after_pop():
    q = Queue()
    q.push(1)
    q.pop()
    q.push(2)
    assert q.peek() == 2
    assert q.pop() == 2
    assert q.empty() is True