class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n < 1:
            return 1

        def is_valid(letter):
            return letter and 1 <= int(letter) <= 26

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s and s[0] != '0' else 0

        for i in range(2, n + 1):
            if 1 <= int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
