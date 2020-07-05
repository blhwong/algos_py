from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [row[:] for row in grid]

        for row in range(1, len(grid)):
            dp[row][0] += dp[row - 1][0]

        for col in range(1, len(grid[0])):
            dp[0][col] += dp[0][col - 1]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                dp[row][col] += min(dp[row - 1][col], dp[row][col - 1])

        return dp[-1][-1]
