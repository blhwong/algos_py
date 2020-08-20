from leet.word_search_2.main import Solution

s = Solution()


def test_1():
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    result = s.findWords(board, ['oath', 'pea', 'eat', 'rain'])
    assert result == ['oath', 'eat']

def test_2():
    board = [['a', 'b']]
    result = s.findWords(board, ['ba'])
    assert result == ['ba']

def test_3():
    board = [
        ['a', 'b', 'c'],
        ['a', 'e', 'd'],
        ['a', 'f', 'g'],
    ]
    result = s.findWords(board, ['abcdefg', 'gfedcbaaa', 'eaabcdgfa', 'befa', 'dgc', 'ade', 'ffffffffff'])
    assert result == ['abcdefg', 'befa', 'eaabcdgfa', 'gfedcbaaa']

def test_4():
    board = [
        ['a', 'a', 'a', 'a'],
        ['a', 'a', 'a', 'a'],
        ['a', 'a', 'a', 'a'],
        ['a', 'a', 'a', 'a'],
        ['b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i'],
        ['j', 'k', 'l', 'm'],
        ['n', 'o', 'p', 'q'],
        ['r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y'],
        ['z', 'z', 'z', 'z'],
    ]
    words = ['aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaab']
    result = s.findWords(board, words)
    assert result == ['aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaab']
