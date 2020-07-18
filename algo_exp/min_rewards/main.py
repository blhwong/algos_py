"""
[8, 4, 2, 1, 3, 6, 7, 9, 5]
 1
 2  1
 3  2  1
 4  3  2  1
 4  3  2  1  2
 4  3  2  1  2  3
 4  3  2  1  2  3  4
 4  3  2  1  2  3  4  5
 4  3  2  1  2  3  4  5  1
"""
def minRewards(scores):
    dp = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            dp[i] = max(dp[i], dp[i - 1] + 1)

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            dp[i] = max(dp[i], dp[i + 1] + 1)

    return sum(dp)
