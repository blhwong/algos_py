class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None] * n for _ in range(m)]
        def move(m_left, n_left):
            if memo[m_left][n_left] is not None:
                return memo[m_left][n_left]
            if m_left == 0 and n_left == 0:
                return 1
            if m_left < 0 or n_left < 0:
                return 0
            memo[m_left][n_left] = (
                move(m_left - 1, n_left) +
                move(m_left, n_left - 1)
            )
            return memo[m_left][n_left]


        res = move(m - 1, n - 1)
        return res

    def uniquePathsIterative(self, m, n):
        dp = [[1] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
