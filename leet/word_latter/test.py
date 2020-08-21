from leet.word_latter.main import Solution

s = Solution()

def test_1():
    result = s.ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
    assert result == 5

def test_2():
    result = s.ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'])
    assert result == 0

def test_3():
    result = s.ladderLength('hit', 'cot', ['hot', 'cot', 'dot', 'dog', 'lot', 'log'])
    assert result == 3

def test_4():
    result = s.ladderLength('hot', 'dog', ['hot', 'dog'])
    assert result == 0
