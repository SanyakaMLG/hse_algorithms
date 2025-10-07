class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            ptr = self.root
            while True:
                if val > ptr.val:
                    if ptr.right is None:
                        ptr.right = Node(val)
                        return
                    ptr = ptr.right
                elif val < ptr.val:
                    if ptr.left is None:
                        ptr.left = Node(val)
                        return
                    ptr = ptr.left
                else:
                    return

    def in_order(self):
        def inner(node):
            if node is None:
                return []
                
            return inner(node.left) + [node.val] + inner(node.right)

        return inner(self.root)

    def pre_order(self):
        def inner(node):
            if node is None:
                return []

            return [node.val] + inner(node.left) + inner(node.right)

        return inner(self.root)

    def post_order(self):
        def inner(node):
            if node is None:
                return []

            return inner(node.left) + inner(node.right) + [node.val]

        return inner(self.root)

    def reverse_in_order(self):
        def inner(node):
            if node is None:
                return []
                
            return inner(node.right) + [node.val] + inner(node.left)

        return inner(self.root)

    def reverse_pre_order(self):
        def inner(node):
            if node is None:
                return []

            return [node.val] + inner(node.right) + inner(node.left)

        return inner(self.root)

    def reverse_post_order(self):
        def inner(node):
            if node is None:
                return []

            return inner(node.right) + inner(node.left) + [node.val]

        return inner(self.root)
