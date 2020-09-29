from algo_exp.longest_palindromic_substring.main import longest_palindromic_substring


def test_1():
    assert longest_palindromic_substring('abaxyzzyxf') == 'xyzzyx'


def test_2():
    assert longest_palindromic_substring('a') == 'a'


def test_3():
    assert longest_palindromic_substring('') == ''
