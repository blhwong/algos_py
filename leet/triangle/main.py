from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [row[:] for row in triangle]

        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    dp[row][col] += dp[row - 1][col]
                elif col == len(triangle[row]) - 1:
                    dp[row][col] += dp[row - 1][col - 1]
                else:
                    dp[row][col] += min(dp[row - 1][col], dp[row - 1][col - 1])

        return min(dp[-1])
