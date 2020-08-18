from algo_exp.bst_construction.main import BST

root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.left.left.left = BST(1)
root.right.left = BST(13)
root.right.right = BST(22)
root.right.left.right = BST(14)



def test_1():
    root.insert(12)
    assert root.right.left.left.value == 12

def test_2():
    root.remove(10)
    assert root.value == 12

def test_3():
    assert root.contains(15) is True

def test_4():
    assert root.contains(100) is False

def test_5():
    root.remove(14)
    assert root.right.left.right is None

def test_6():
    single = BST(1)
    single.right = BST(2)
    single.remove(3)
    assert single.value == 1
    assert single.right.value == 2
