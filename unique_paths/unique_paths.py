class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[None] * n for _ in range(m)]
        def move(m_left, n_left, trail):
            if memo[m_left][n_left]:
                return memo[m_left][n_left]
            if m_left == 0 and n_left == 0:
                return 1
            if m_left < 0 or n_left < 0:
                return 0
            memo[m_left][n_left] = (
                move(m_left - 1, n_left, trail + 'R') +
                move(m_left, n_left - 1, trail + 'D')
            )
            return memo[m_left][n_left]


        res = move(m - 1, n - 1, '')
        return res