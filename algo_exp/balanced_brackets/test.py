from algo_exp.balanced_brackets.main import balanced_brackets


def test_1():
    assert balanced_brackets('([])(){}(())()()') is True


def test_2():
    assert balanced_brackets('[(])') is False


def test_3():
    assert balanced_brackets('(a)') is True
