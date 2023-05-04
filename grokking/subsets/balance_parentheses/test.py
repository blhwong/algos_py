from grokking.subsets.balance_parentheses.main import generate_valid_parentheses, generate_valid_parentheses_recursive

def test_1():
    expected = ['(())', '()()']
    assert generate_valid_parentheses(2) == expected

def test_2():
    expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert generate_valid_parentheses(3) == expected

def test_3():
    expected = ['(())', '()()']
    assert generate_valid_parentheses_recursive(2) == expected

def test_4():
    expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
    assert generate_valid_parentheses_recursive(3) == expected
