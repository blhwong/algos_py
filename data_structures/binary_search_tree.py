from collections import deque
from data_structures.tree_node import TreeNode

class BST(TreeNode):
    def __init__(self, value):
        self.value = value
        self.val = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
