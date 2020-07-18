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
            dp[curr] = dp[prev] + 1
        else:
            while prev >= 0 and scores[prev] > scores[prev + 1]:
                dp[prev] = max(dp[prev], dp[prev + 1] + 1)
                prev -= 1

    return sum(dp)
