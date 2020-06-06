import unittest
from unittest import TestCase, main
from leet.sudoku_solver.main import Solution

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        s.solveSudoku(board)
        expected = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
        ]
        self.assertListEqual(board, expected)

    def test_2(self):
        board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
        s.solveSudoku(board)
        expected = [["5", "1", "9", "7", "4", "8", "6", "3", "2"], ["7", "8", "3", "6", "5", "2", "4", "1", "9"], ["4", "2", "6", "1", "3", "9", "8", "7", "5"], ["3", "5", "7", "9", "8", "6", "2", "4", "1"], [
            "2", "6", "4", "3", "1", "7", "5", "9", "8"], ["1", "9", "8", "5", "2", "4", "3", "6", "7"], ["9", "7", "5", "8", "6", "3", "1", "2", "4"], ["8", "3", "2", "4", "9", "1", "7", "5", "6"], ["6", "4", "1", "2", "7", "5", "9", "8", "3"]]
        self.assertListEqual(board, expected)

    @unittest.skip('long test')
    def test_3(self):
        board=[[".",".",".","2",".",".",".","6","3"],["3",".",".",".",".","5","4",".","1"],[".",".","1",".",".","3","9","8","."],[".",".",".",".",".",".",".","9","."],[".",".",".","5","3","8",".",".","."],[".","3",".",".",".",".",".",".","."],[".","2","6","3",".",".","5",".","."],["5",".","3","7",".",".",".",".","8"],["4","7",".",".",".","1",".",".","."]]
        s.solveSudoku(board)
        expected = [['8', '5', '4', '2', '1', '9', '7', '6', '3'], ['3', '9', '7', '8', '6', '5', '4', '2', '1'], ['2', '6', '1', '4', '7', '3', '9', '8', '5'], ['7', '8', '5', '1', '2', '6', '3', '9', '4'], [
            '6', '4', '9', '5', '3', '8', '1', '7', '2'], ['1', '3', '2', '9', '4', '7', '8', '5', '6'], ['9', '2', '6', '3', '8', '4', '5', '1', '7'], ['5', '1', '3', '7', '9', '2', '6', '4', '8'], ['4', '7', '8', '6', '5', '1', '2', '3', '9']]
        self.assertListEqual(board, expected)


if __name__ == '__main__':
    main()
