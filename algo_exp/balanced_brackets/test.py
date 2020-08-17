from algo_exp.balanced_brackets.main import balancedBrackets


def test_1():
    assert balancedBrackets('([])(){}(())()()') is True

def test_2():
    assert balancedBrackets('[(])') is False

def test_3():
    assert balancedBrackets('(a)') is True
