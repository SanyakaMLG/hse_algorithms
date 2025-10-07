from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def validate_bst(root: Optional[Node]):
    def inner_validate(node: Optional[Node], upper, lower):
        if node is None:
            return True

        if node.val >= upper or node.val <= lower:
            return False

        return inner_validate(node.left, node.val, lower) and inner_validate(node.right, upper, node.val)

    return inner_validate(root, float('inf'), -float('inf'))