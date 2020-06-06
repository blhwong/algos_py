class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return 1
        prev1 = 1
        prev2 = 2
        ans = None
        for i in range(3, n + 1):
            ans = prev2 + prev1
            prev1 = prev2
            prev2 = ans
        return ans or prev2

    def bottom_up(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [None for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs(self, n: int) -> int:
        memo = [None for _ in range(n + 1)]
        def climb(steps):
            if memo[steps]:
                return memo[steps]
            if steps == 0:
                return 1
            if steps < 0:
                return 0
            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]
        return climb(n)
