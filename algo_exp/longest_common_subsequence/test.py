from algo_exp.longest_common_subsequence.main import longestCommonSubsequence


def test_1():
    assert longestCommonSubsequence('ZXVVYZW', 'XKYKZPW') == ['X', 'Y', 'Z', 'W']

def test_2():
    assert longestCommonSubsequence('clement', 'antoine') == ['n', 't']

def test_3():
    assert longestCommonSubsequence('abcba', 'abcbcba') == ['a', 'b', 'c', 'b', 'a']
