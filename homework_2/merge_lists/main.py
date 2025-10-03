from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def copy(self) -> Optional['Node']:
        if self is None:
            return None

        new_head = Node(self.val)
        current_original = self.next
        current_copy = new_head

        while current_original is not None:
            current_copy.next = Node(current_original.val)
            current_copy = current_copy.next
            current_original = current_original.next

        return new_head

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

    def __repr__(self):
        vals = []
        current = self
        while current:
            vals.append(str(current.val))
            current = current.next
        return " -> ".join(vals) + " -> None"


def merge_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    if not list1 and not list2:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    first = list1.copy()
    second = list2.copy()

    res = None
    if first.val <= second.val:
        res = first
        first = first.next
    else:
        res = second
        second = second.next

    cur = res
    while first and second:
        if first.val <= second.val:
            cur.next = first
            first = first.next
        else:
            cur.next = second
            second = second.next

        cur = cur.next

    cur.next = first or second

    return res


def merge_lists_dummy(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    dummy = Node(None)
    cur = dummy

    first = list1.copy() if list1 is not None else None
    second = list2.copy() if list2 is not None else None
    
    while first and second:
        if first.val <= second.val:
            cur.next = first
            first = first.next
        else:
            cur.next = second
            second = second.next

        cur = cur.next
        
    cur.next = first or second

    return dummy.next
            