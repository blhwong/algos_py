"""
          5   11  3   50  60  90
    0     0   0   0   0   0   0
    1     0   6   6   47  57  87
    2     0   6   6   53  63  93

"""
def maxProfitWithKTransactions(prices, k):
    if not prices:
        return 0

    dp = [[0] * len(prices) for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_prev = -float('inf')
        for j in range(1, len(prices)):
            hold = dp[i][j - 1]
            max_prev = max(max_prev, dp[i - 1][j - 1] - prices[j - 1])

            sell = max_prev + prices[j]

            dp[i][j] = max(hold, sell)


    return dp[-1][-1]
