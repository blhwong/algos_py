from algo_exp.number_of_binary_tree_topologies.main import numberOfBinaryTreeTopologies


def test_1():
    assert numberOfBinaryTreeTopologies(3) == 5

def test_2():
    assert numberOfBinaryTreeTopologies(0) == 1
