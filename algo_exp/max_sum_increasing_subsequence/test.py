from algo_exp.max_sum_increasing_subsequence.main import maxSumIncreasingSubsequence


def test_1():
    assert maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]) == [110, [10, 20, 30, 50]]


def test_2():
    assert maxSumIncreasingSubsequence([-1]) == [-1, [-1]]


def test_3():
    assert maxSumIncreasingSubsequence([-5, -4, -3, -2, -1]) == [-1, [-1]]

def test_4():
    assert maxSumIncreasingSubsequence([-1, 1]) == [1, [1]]
