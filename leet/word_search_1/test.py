from leet.word_search_1.main import Solution


s = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
]


def test_1():
    assert s.exist(board, 'ABCCED') is True


def test_2():
    assert s.exist(board, 'SEE') is True


def test_3():
    assert s.exist(board, 'ABCB') is False

def test_4():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'E', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    assert s.exist(board, 'ABCESEEEFS') is True
