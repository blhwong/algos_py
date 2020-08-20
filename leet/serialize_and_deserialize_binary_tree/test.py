from leet.serialize_and_deserialize_binary_tree.main import Codec
from data_structures.tree_node import TreeNode

c = Codec()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

def test_serialize():
    assert c.serialize(root) == '[1, 2, null, null, 3, 4, null, null, 5, null, null]'

def test_deserialize():
    res = c.deserialize('[1, 2, null, null, 3, 4, null, null, 5, null, null]')
    print(res)
    assert res.val == 1
    assert res.left.val == 2
    assert res.left.left is None
    assert res.left.right is None
    assert res.right.val == 3
    assert res.right.left.val == 4
    assert res.right.right.val == 5
