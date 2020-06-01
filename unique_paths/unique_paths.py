class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tracker = {}
        def move(m_left, n_left, trail):
            key = f'{m_left},{n_left}'
            if key in tracker:
                return tracker[key]
            if m_left == 0 and n_left == 0:
                return 1
            if m_left < 0 or n_left < 0:
                return 0
            tracker[key] = (
                move(m_left - 1, n_left, trail + 'R') +
                move(m_left, n_left - 1, trail + 'D')
            )
            return tracker[key]


        return move(m - 1, n - 1, '')

