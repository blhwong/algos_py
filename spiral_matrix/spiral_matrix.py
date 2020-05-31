from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        class Spiral:
            def __init__(self, matrix):
                self.ans = []
                self.row = 0
                self.col = 0
                self.matrix = matrix
                self.visited = [[False] * len(matrix[0])
                                for _ in range(len(matrix))]
                self.unvisited = len(matrix) * len(matrix[0])

            def can_continue(self, row, col):
                matrix = self.matrix
                return (
                    0 <= row < len(matrix) and
                    0 <= col < len(matrix[0]) and
                    not self.visited[row][col]
                )

            def add_to_list(self, row, col):
                if not self.visited[row][col]:
                    self.ans.append(matrix[row][col])
                    self.visited[row][col] = True
                    self.unvisited -= 1

            def visit(self, row_delta, col_delta):
                row, col = self.row, self.col
                self.add_to_list(row, col)
                if self.can_continue(row + row_delta, col + col_delta):
                    self.row += row_delta
                    self.col += col_delta
                    self.visit(row_delta, col_delta)

            def go_right(self):
                self.visit(0, 1)

            def go_down(self):
                self.visit(1, 0)

            def go_left(self):
                self.visit(0, -1)

            def go_up(self):
                self.visit(-1, 0)

            def solve(self):
                while self.unvisited > 0:
                    self.go_right()
                    self.go_down()
                    self.go_left()
                    self.go_up()
                return self.ans

        spiral = Spiral(matrix)
        spiral.solve()
        return spiral.ans
