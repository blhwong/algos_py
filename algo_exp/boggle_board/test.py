from unittest import TestCase, main
from algo_exp.boggle_board.main import boggleBoard


class TestSuite(TestCase):
    def test_1(self):
        board = [
            ['t', 'h', 'i', 's', 'i', 's', 'a'],
            ['s', 'i', 'm', 'p', 'l', 'e', 'x'],
            ['b', 'x', 'x', 'x', 'x', 'e', 'b'],
            ['x', 'o', 'g', 'g', 'l', 'x', 'o'],
            ['x', 'x', 'x', 'D', 'T', 'r', 'a'],
            ['R', 'E', 'P', 'E', 'A', 'd', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['N', 'O', 'T', 'R', 'E', '-', 'P'],
            ['x', 'x', 'D', 'E', 'T', 'A', 'E']
        ]
        words = [
            'this',
            'is',
            'not',
            'a',
            'simple',
            'boggle',
            'board',
            'test',
            'REPEATED',
            'NOTRE-PEATED'
        ]
        expected = [
            'this',
            'is',
            'a',
            'simple',
            'boggle',
            'board',
            'NOTRE-PEATED'
        ]
        self.assertCountEqual(boggleBoard(board, words), expected)

    def test_2(self):
        board = [
            ['c', 'o', 'm'],
            ['r', 'p', 'l'],
            ['c', 'i', 't'],
            ['o', 'a', 'e'],
            ['f', 'o', 'd'],
            ['z', 'r', 'b'],
            ['g', 'i', 'a'],
            ['o', 'a', 'g'],
            ['f', 's', 'z'],
            ['t', 'e', 'i'],
            ['t', 'w', 'd']
        ]
        words = [
            'commerce',
            'complicated',
            'twisted',
            'zigzag',
            'comma',
            'foobar',
            'baz',
            'there'
        ]
        expected = [
            'complicated',
            'foobar',
            'twisted',
            'zigzag',
        ]
        self.assertCountEqual(boggleBoard(board, words), expected)


if __name__ == '__main__':
    main()
