from typing import List

def get_tracker():
    return {f'{i}': 0 for i in range(1, 10)}

def is_valid_horizontal(board, row, col_len):
    tracker = get_tracker()
    for col in range(col_len):
        curr = board[row][col]
        if curr == '.':
            return False
        tracker[curr] += 1
        if tracker[curr] > 1:
            return False
    return True

def is_valid_vertical(board, col, row_len):
    tracker = get_tracker()
    for row in range(row_len):
        curr = board[row][col]
        if curr == '.':
            return False
        tracker[curr] += 1
        if tracker[curr] > 1:
            return False
    return True

def is_valid_square(board, start_row, start_col):
    tracker = get_tracker()
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            curr = board[row][col]
            if curr == '.':
                return False
            tracker[curr] += 1
            if tracker[curr] > 1:
                return False
    return True

def is_valid_sudoku(board):
    for row_idx, row in enumerate(board):
        if not is_valid_horizontal(board, row_idx, len(row)):
            return False

    for col_idx, col in enumerate(board[0]):
        if not is_valid_vertical(board, col_idx, len(board)):
            return False

    for row in range(0, len(board), 3):
        for col in range(0, len(board[0]), 3):
            if not is_valid_square(board, row, col):
                return False

    return True


def remove_from_possibilities(board, possibilities, row, col, val):
    updated_possibilities = possibilities.copy()
    new_board = [row.copy() for row in board]
    for i in range(9):
        key = (i, col)
        if key in updated_possibilities:
            updated_possibilities[key].discard(val)
            if len(updated_possibilities[key]) == 1:
                v = updated_possibilities[key].pop()
                new_board[i][col] = v
                del updated_possibilities[key]
                updated_possibilities, new_board = remove_from_possibilities(new_board, updated_possibilities, i, col, v)

    for j in range(9):
        key = (row, j)
        if key in updated_possibilities:
            updated_possibilities[key].discard(val)
            if len(updated_possibilities[key]) == 1:
                v = updated_possibilities[key].pop()
                new_board[row][j] = v
                del updated_possibilities[key]
                updated_possibilities, new_board = remove_from_possibilities(new_board, updated_possibilities, row, j, v)

    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            key = (i, j)
            if key in updated_possibilities:
                updated_possibilities[key].discard(val)
                if len(updated_possibilities[key]) == 1:
                    v = updated_possibilities[key].pop()
                    new_board[i][j] = v
                    del updated_possibilities[key]
                    updated_possibilities, new_board = remove_from_possibilities(new_board, updated_possibilities, i, j, v)

    return updated_possibilities, new_board

def get_possibilities(board):
    possibilities = {}
    new_board = [row.copy() for row in board]
    for row in range(9):
        for col in range(9):
            if new_board[row][col] != '.':
                continue

            choices = set([str(i) for i in range(1, 10)])

            for i in range(9):
                choices.discard(new_board[i][col])

            for j in range(9):
                choices.discard(new_board[row][j])

            start_row, start_col = (row // 3) * 3, (col // 3) * 3

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    choices.discard(new_board[i][j])

            if len(choices) == 1:
                val = choices.pop()
                new_board[row][col] = val
                possibilities, new_board = remove_from_possibilities(new_board, possibilities, row, col, val)
            else:
                possibilities[(row, col)] = choices

    return possibilities, new_board

def solve(board):
    possibilities, new_board = get_possibilities(board)
    if not len(possibilities):
        if is_valid_sudoku(new_board):
            return True, new_board
        return False, board

    item = min(possibilities.items(), key = lambda x: len(x[1]))
    key, shortest_possibilities = item
    row, col = key
    saved_board = [row.copy() for row in board]
    for p in shortest_possibilities:
        board[row][col] = p
        p, new_board = get_possibilities(board)
        solved, ans = solve(new_board)
        if solved:
            return solved, ans
        else:
            board = saved_board

    return False, board


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solved, ans = solve(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = ans[i][j]
