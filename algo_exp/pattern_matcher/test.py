from algo_exp.pattern_matcher.main import patternMatcher


def test_1():
    result = patternMatcher('xxyxxy', 'gogopowerrangergogopowerranger')
    expected = ['go', 'powerranger']
    assert result == expected

def test_2():
    result = patternMatcher('yyxyyx', 'gogopowerrangergogopowerranger')
    expected = ['powerranger', 'go']
    assert result == expected

def test_3():
    result = patternMatcher('xxx', 'blahblahblah')
    expected = ['blah', '']
    assert result == expected

def test_4():
    result = patternMatcher('yyyy', 'testtesttesttest')
    expected = ['', 'test']
    assert result == expected
