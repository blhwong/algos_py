from algo_exp.palindrome_check.main import is_palindrome


def test_1():
    assert is_palindrome('abcdcba') is True

def test_2():
    assert is_palindrome('abcde') is False
