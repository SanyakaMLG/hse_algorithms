class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"(val: {self.val}, next: {self.next})"


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def _pop(self):
        self.head = self.head.next

    def peek(self):
        if self.empty():
            raise IndexError("stack is empty")
        return self.head.val

    def pop(self):
        return_val = self.peek()
        self._pop()
        return return_val

    def empty(self):
        return self.head is None
            