from typing import List


class Solution:

    def found(self, board, row, col, i, word, visited):
        if i == len(word):
            return True
        if not 0 <= row < len(visited):
            return False
        if not 0 <= col < len(visited[0]):
            return False
        if word[i] != board[row][col]:
            return False
        if visited[row][col]:
            return False
        visited[row][col] = True
        if (
            self.found(board, row + 1, col, i + 1, word, visited) or
            self.found(board, row - 1, col, i + 1, word, visited) or
            self.found(board, row, col + 1, i + 1, word, visited) or
            self.found(board, row, col - 1, i + 1, word, visited)
        ):
            return True
        visited[row][col] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
                    if self.found(board, row, col, 0, word, visited):
                        return True

        return False
