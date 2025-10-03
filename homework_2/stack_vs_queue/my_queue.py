class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        if self.prev is None:
            return f"(prev: None, val: {self.val}, next: {self.next})"
        return f"(<- prev, val: {self.val}, next: {self.next})"


class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def peek(self):
        if self.empty():
            raise IndexError("queue is empty")
        return self.tail.prev.val

    def _pop(self):
        pop_node = self.tail.prev
        self.tail.prev = pop_node.prev
        pop_node.prev.next = self.tail

    def pop(self):
        return_val = self.peek()
        self._pop()
        return return_val

    def empty(self):
        return self.head.next == self.tail
        