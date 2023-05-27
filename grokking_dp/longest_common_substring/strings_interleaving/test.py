from grokking_dp.longest_common_substring.strings_interleaving.main import find_si


def test_1():
    assert not find_si("abd", "cef", "adcbef")


def test_2():
    assert not find_si("abc", "def", "abdccf")


def test_3():
    assert find_si("abcdef", "mnop", "mnaobcdepf")


def test_4():
    assert find_si("aabcc", "dbbca", "aadbbcbcac")
