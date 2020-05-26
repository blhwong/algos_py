from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_tracker():
            return {f'{i}': 0 for i in range(1, 10)}


        def is_valid_horizontal(row, col_len):
            tracker = get_tracker()
            for col in range(col_len):
                curr = board[row][col]
                if curr == '.':
                    continue
                tracker[curr] += 1
                if tracker[curr] > 1:
                    return False
            return True

        def is_valid_vertical(col, row_len):
            tracker = get_tracker()
            for row in range(row_len):
                curr = board[row][col]
                if curr == '.':
                    continue
                tracker[curr] += 1
                if tracker[curr] > 1:
                    return False
            return True

        def is_valid_square(start_row, start_col):
            tracker = get_tracker()
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    curr = board[row][col]
                    if curr == '.':
                        continue
                    tracker[curr] += 1
                    if tracker[curr] > 1:
                        return False
            return True


        for row_idx, row in enumerate(board):
            if not is_valid_horizontal(row_idx, len(row)):
                return False

        for col_idx, col in enumerate(board[0]):
            if not is_valid_vertical(col_idx, len(board)):
                return False

        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                if not is_valid_square(row, col):
                    return False

        return True
