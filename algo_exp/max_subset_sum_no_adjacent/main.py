def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0

    dp = [0] * (len(array) + 1)
    dp[1] = array[0]
    for i in range(2, len(array) + 1):
        dp[i] = max(dp[i - 1], array[i - 1] + dp[i - 2])

    return dp[-1]
