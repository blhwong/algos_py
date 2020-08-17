from algo_exp.longest_palindromic_substring.main import longestPalindromicSubstring


def test_1():
    assert longestPalindromicSubstring('abaxyzzyxf') == 'xyzzyx'

def test_2():
    assert longestPalindromicSubstring('a') == 'a'

def test_3():
    assert longestPalindromicSubstring('') == ''
