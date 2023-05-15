from grokking_dp.knapsack_dp.equal_subset_sum_partition.main import can_partition_recursive, can_partition_iterative


def test_1():
    assert can_partition_recursive([1, 2, 3, 4])

def test_2():
    assert can_partition_recursive([1, 1, 3, 4, 7])

def test_3():
    assert not can_partition_recursive([2, 3, 4, 6])

def test_4():
    assert can_partition_recursive([2, 4, 2, 16, 16, 2, 2, 4, 5, 5, 10, 6, 32, 6, 12])

def test_5():
    assert not can_partition_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 500])

def test_6():
    assert can_partition_iterative([1, 2, 3, 4])

def test_7():
    assert can_partition_iterative([1, 1, 3, 4, 7])

def test_8():
    assert not can_partition_iterative([2, 3, 4, 6])

def test_9():
    assert can_partition_iterative([2, 4, 2, 16, 16, 2, 2, 4, 5, 5, 10, 6, 32, 6, 12])

def test_10():
    assert not can_partition_iterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 500])

def test_11():
    assert not can_partition_iterative([1, 1, 4])
