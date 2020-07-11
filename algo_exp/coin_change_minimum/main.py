def minNumberOfCoinsForChange(n, denoms):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for coin in denoms:
        for i in range(coin, n + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)


    return dp[-1] if dp[-1] != float('inf') else -1
