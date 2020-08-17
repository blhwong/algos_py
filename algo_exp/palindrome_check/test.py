from algo_exp.palindrome_check.main import isPalindrome


def test_1():
    assert isPalindrome('abcdcba') is True

def test_2():
    assert isPalindrome('abcde') is False
