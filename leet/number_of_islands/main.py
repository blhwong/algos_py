from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(row, col, visited):
            if not 0 <= row < len(grid):
                return
            if not 0 <= col < len(grid[0]):
                return
            if (row, col) in visited:
                return
            if grid[row][col] == '0':
                return
            visited.add((row, col))
            traverse(row, col + 1, visited)
            traverse(row + 1, col, visited)
            traverse(row, col - 1, visited)
            traverse(row - 1, col, visited)

        visited = set()
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == '1':
                    ans += 1
                    traverse(row, col, visited)

        return ans
