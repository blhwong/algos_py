from leet.word_break.main import Solution

s = Solution()

def test_1():
    assert s.wordBreak('leetcode', ['leet', 'code']) is True

def test_2():
    assert s.wordBreak('applepenapple', ['apple', 'pen']) is True

def test_3():
    assert s.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) is False
