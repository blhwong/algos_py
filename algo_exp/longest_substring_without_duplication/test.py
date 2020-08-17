from algo_exp.longest_substring_without_duplication.main import longestSubstringWithoutDuplication


def test_1():
    assert longestSubstringWithoutDuplication('clementisacap') == 'mentisac'

def test_2():
    assert longestSubstringWithoutDuplication('abcb') == 'abc'
