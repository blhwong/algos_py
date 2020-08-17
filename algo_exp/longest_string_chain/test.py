from algo_exp.longest_string_chain.main import longestStringChain

def test_1():
    result = longestStringChain([
        'abde',
        'abc',
        'abd',
        'abcde',
        'ade',
        'ae',
        'labde',
        'abcdef',
    ])
    expected = [
        'abcdef',
        'abcde',
        'abde',
        'ade',
        'ae',
    ]
    assert result == expected
