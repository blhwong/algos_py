from grokking.sliding_window.non_repeat_substring.main import non_repeat_substring


def test_1():
    assert non_repeat_substring('aabccbb') == 3

def test_2():
    assert non_repeat_substring('abbbb') == 2

def test_3():
    assert non_repeat_substring('abccde') == 3
