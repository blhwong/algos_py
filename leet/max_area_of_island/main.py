from typing import List


class Solution:

    def get_area(self, grid, row, col, visited):
        if not 0 <= row < len(grid):
            return 0
        if not 0 <= col < len(grid[0]):
            return 0
        if grid[row][col] == 0:
            return 0
        if (row, col) in visited:
            return 0
        visited.add((row, col))
        return 1 + (
            self.get_area(grid, row + 1, col, visited) +
            self.get_area(grid, row, col + 1, visited) +
            self.get_area(grid, row - 1, col, visited) +
            self.get_area(grid, row, col - 1, visited)
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    ans = max(ans, self.get_area(grid, row, col, visited))

        return ans
