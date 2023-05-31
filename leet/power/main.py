class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}
        if n < 0:
            return self.recurse(1/x, -n, dp)
        return self.recurse(x, n, dp)

    def recurse(self, x: float, n: int, dp) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n in dp:
            return dp[n]
        left = n // 2
        right = n - n // 2
        dp[n] = self.recurse(x, left, dp) * self.recurse(x, right, dp)
        return dp[n]
