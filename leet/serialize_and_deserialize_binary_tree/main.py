# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from data_structures.tree_node import TreeNode
from json import loads, dumps
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def traverse(curr, array):
            if not curr:
                array.append(None)
                return
            array.append(curr.val)
            traverse(curr.left, array)
            traverse(curr.right, array)

        ans = []
        traverse(root, ans)
        return dumps(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def traverse(q):
            if not q:
                return None
            val = q.popleft()
            if val is None:
                return val
            curr = TreeNode(val)
            curr.left = traverse(q)
            curr.right = traverse(q)

            return curr


        q = deque(loads(data))
        return traverse(q)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
