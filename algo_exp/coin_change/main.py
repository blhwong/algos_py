def numberOfWaysToMakeChange(n, denoms):
    if not denoms:
        return 0

    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in denoms:
        for i in range(coin, n + 1):
                dp[i] += dp[i - coin]

    return dp[-1]
