from algo_exp.multi_string_search.main import multiStringSearch


def test_1():
    result = multiStringSearch('this is a big string', ['this', 'yo', 'is', 'a', 'bigger', 'string', 'kappa'])
    expected = [True, False, True, True, False, True, False]
    assert result == expected

def test_2():
    result = multiStringSearch('Mary goes to the shopping center every week', ['to', 'Mary', 'centers', 'shop', 'shopping', 'string', 'kappa'])
    expected = [True, True, False, True, True, False, False]
    assert result == expected

def test_3():
    result = multiStringSearch('this ain't a big string', ['this', 'is', 'yo', 'a', 'bigger'])
    expected = [True, True, False, True, False]
    assert result == expected

def test_4():
    result = multiStringSearch('adcb akfkw afnmc fkadn vkaca jdaf jacb cdba cbda', ['abcd', 'acbd', 'adbc', 'dabc', 'cbda', 'cabd', 'cdab'])
    expected = [False, False, False, False, True, False, False]
    assert result == expected
