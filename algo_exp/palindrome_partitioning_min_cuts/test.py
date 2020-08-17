from algo_exp.palindrome_partitioning_min_cuts.main import palindromePartitioningMinCuts


def test_1():
    assert palindromePartitioningMinCuts('noonabbad') == 2

def test_2():
    assert palindromePartitioningMinCuts('a') == 0

def test_3():
    assert palindromePartitioningMinCuts('abbba') == 0

def test_4():
    assert palindromePartitioningMinCuts('ababbbabbababa') == 3
