from algo_exp.longest_peak.main import longestPeak


def test_1():
    assert longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]) == 6

def test_2():
    assert longestPeak([1, 3, 2]) == 3

def test_3():
    assert longestPeak([1, 2, 3]) == 0
