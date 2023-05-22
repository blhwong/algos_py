from grokking_dp.palindromic_subsequence.palindromic_partitioning.main import find_mpp_cuts


def test_1():
    assert find_mpp_cuts("abdbca") == 3


def test_2():
    assert find_mpp_cuts("cddpd") == 2


def test_3():
    assert find_mpp_cuts("pqr") == 2


def test_4():
    assert find_mpp_cuts("pp") == 0
