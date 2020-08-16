from algo_exp.balanced_brackets.main import balancedBrackets


def test_1():
    assert balancedBrackets('([])(){}(())()()')

def test_2():
    assert not balancedBrackets('[(])')

def test_3():
    assert balancedBrackets('(a)')
