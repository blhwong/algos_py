"""
       0   75   105   120   75   90   135
75    75   75    75    75   75   75    75
105  105   105  105   105  105  105   105
120  105   105  195   195  195  195   195
75   105   105  195   195  195  195   195
90   105   105  195   195  195  285   285
135  105   105  195   195  195  285   330

0  75  105  195  195  285  330
"""

def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0

    dp = [0] * (len(array) + 1)
    dp[1] = array[0]
    for i in range(2, len(array) + 1):
        dp[i] = max(dp[i - 1], array[i - 1] + dp[i - 2])

    return dp[-1]
