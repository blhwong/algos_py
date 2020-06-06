from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        class Possibilities:
            def __repr__(self):
                return f'{self.__dict__}'

            def __init__(self, row, col):
                self.row = row
                self.col = col
                p = {f'{i}': True for i in range(1, 10)}
                for i in range(9):
                    curr = board[i][col]
                    if curr == '.':
                        continue
                    if curr in p:
                        del p[board[i][col]]
                for j in range(9):
                    curr = board[row][j]
                    if board == '.':
                        continue
                    if curr in p:
                        del p[board[row][j]]
                start_row = (row // 3) * 3
                start_col = (col // 3) * 3
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        curr = board[i][j]
                        if curr == '.':
                            continue
                        if curr in p:
                            del p[board[i][j]]
                self.choices = p

            def remove(self, val):
                choices = self.choices
                if val in choices.keys():
                    # print('removing', val)
                    del choices[val]
                    self.choices = choices

            def add(self, val):
                choices = self.choices
                if val not in choices.keys():
                    choices[val] = True
                    self.choices = choices

            def copy(self):
                p = Possibilities(self.row, self.col)
                p.choices = {f'{i}': True for i in self.choices.keys()}
                return p



        class Tracker:
            def __repr__(self):
                return f'{self.__dict__}'

            def __init__(self):
                self.storage = {}
                self.unknown = 0

            def get_p(self, row, col):
                return self.storage.get(row, {}).get(col, None)

            def set_p(self, row, col, p):
                # print('setting p')
                if not self.storage.get(row):
                    self.storage[row] = {}
                self.storage[row][col] = p

            def del_p(self, row, col):
                # print('deleting p')
                if self.storage.get(row, {}).get(col):
                    del self.storage[row][col]
                    if not self.storage[row]:
                        del self.storage[row]

            def set_board(self, row, col, val):
                # print('setting', row, col, val)
                board[row][col] = val
                if self.get_p(row, col):
                    self.del_p(row, col)
                    self.unknown -= 1
                self.fix(row, col, val)

            def get_copy(self):
                copy = Tracker()
                copy.unknown = self.unknown
                for row in self.storage.keys():
                    for col in self.storage[row].keys():
                        p = self.get_p(row, col)
                        copy.set_p(row, col, p.copy())
                return copy


            def add(self, p):
                row, col = p.row, p.col
                if len(p.choices) == 1:
                    # print('only 1 possibility')
                    self.set_board(row, col, list(p.choices.keys())[0])
                else:
                    # print(row, col)
                    self.unknown += 1
                    self.set_p(row, col, p)

            def fix(self, row, col, val, choice = None):
                # print('fixing')
                # print(self.storage)
                for i in range(9):
                    # print(i, col)
                    p = self.get_p(i, col)
                    if p:
                        # print('row', p)
                        p.remove(val)
                        if len(p.choices) == 1:
                            self.set_board(i, col, list(p.choices.keys())[0])
                for j in range(9):
                    p = self.get_p(row, j)
                    if p:
                        # print('col', p)
                        p.remove(val)
                        if len(p.choices) == 1:
                            self.set_board(row, j, list(p.choices.keys())[0])
                start_row = (row // 3) * 3
                start_col = (col // 3) * 3
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        p = self.get_p(i, j)
                        if p:
                            # print('curr', p)
                            p.remove(val)
                            if len(p.choices) == 1:
                                self.set_board(i, j, list(p.choices.keys())[0])

        t = Tracker()
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    continue
                p = Possibilities(row, col)
                t.add(p)

        # print(t)
        # print('\n')
        # print(board)
        if t.unknown == 0:
            return

        def is_valid_sudoku(board: List[List[str]]) -> bool:
            def get_tracker():
                return {f'{i}': 0 for i in range(1, 10)}

            def is_valid_horizontal(row, col_len):
                tracker = get_tracker()
                for col in range(col_len):
                    curr = board[row][col]
                    if curr == '.':
                        return False
                    tracker[curr] += 1
                    if tracker[curr] > 1:
                        return False
                return True

            def is_valid_vertical(col, row_len):
                tracker = get_tracker()
                for row in range(row_len):
                    curr = board[row][col]
                    if curr == '.':
                        return False
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
                            return False
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

        def solve(t):
            if t.unknown == 0:
                # print('no more unknowns', board, t)
                return is_valid_sudoku(board)

            for row in t.storage.keys():
                for col in t.storage[row].keys():
                    p = t.storage[row][col]
                    choices = p.choices
                    # print(choices, row, col)
                    for choice in choices:
                        # print('choice', choice)
                        # print('original before', t)
                        copy = t.get_copy()
                        copy.set_board(row, col, choice)
                        # print('cp', copy)
                        # print('original', t)
                        solved = solve(copy)
                        # print('solved?', solved)
                        if solved:
                            return True
            return False

        # print('Needs guessing')
        solve(t)

