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
    for curr in range(1, len(scores)):
        prev = curr - 1
        if scores[curr] > scores[prev]:
            dp[curr] = max(dp[curr], dp[prev] + 1)

    for curr in reversed(range(len(scores) - 1)):
        prev = curr + 1
        if scores[curr] > scores[prev]:
            dp[curr] = max(dp[curr], dp[prev] + 1)

    return sum(dp)
