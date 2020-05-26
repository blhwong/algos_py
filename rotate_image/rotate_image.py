from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copy = [row[:] for row in matrix]

        def swap(i, j, k, l):
            matrix[k][l] = copy[i][j]


        def get_swap_indices(row, col):
            return col, len(matrix) - row - 1


        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                k, l = get_swap_indices(i, j)
                swap(i, j, k, l)

