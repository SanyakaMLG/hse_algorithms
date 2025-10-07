from typing import Optional

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[Node]) -> bool:
    def check_depth(node: Optional[Node]) -> int:
        if node is None:
            return 0

        left_depth = check_depth(node.left)
        if left_depth == -1:
            return -1

        right_depth = check_depth(node.right)
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1
        
    return check_depth(root) != -1