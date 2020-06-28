def spiralTraverse(array):
    class Spiral:
        def __init__(self, matrix):
            self.row_count = len(matrix)
            self.col_count = len(matrix[0])
            self.ans = []
            self.row = 0
            self.col = 0
            self.visited = [[False] * self.col_count for _ in range(self.row_count)]
            self.matrix = matrix
            self.count = 0

        def can_visit(self, row, col):
            return (
                0 <= row < self.row_count and
                0 <= col < self.col_count and
                not self.visited[row][col]
            )

        def add_to_list(self, row, col):
            if not self.visited[row][col]:
                self.ans.append(self.matrix[row][col])
                self.count += 1
                self.visited[row][col] = True

        def visit(self, row_delta, col_delta):
            row, col = self.row, self.col
            self.add_to_list(row, col)
            if self.can_visit(row + row_delta, col + col_delta):
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
            while self.count < self.row_count * self.col_count:
                self.go_right()
                self.go_down()
                self.go_left()
                self.go_up()
            return self.ans

    spiral = Spiral(array)

    return spiral.solve()
