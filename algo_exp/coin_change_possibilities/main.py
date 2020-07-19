"""
   0  1  2  3  4  5  6  7  8  9  10
1  1  1  1  1  1  1  1  1  1  1  1
5  1  1  1  1  1  2  2  2  2  2  3
10 1  1  1  1  1  2  2  2  2  2  4
"""

def numberOfWaysToMakeChange(n, denoms):
    if not denoms:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in denoms:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[-1]
