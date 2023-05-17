"""
Introduction
We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. We need to cut the ribbon into the maximum number of pieces that comply with the above-mentioned possible lengths. Write a method that will return the count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
Example 2:

n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
Example 3:

n: 13
Ribbon Lengths: {3,5,7}
Output: 3
Explanation: Ribbon pieces will be {3,3,7}.
"""


def count_ribbon_pieces(ribbon_lengths, total):
    dp = [[-float('infinity')] * (total + 1) for _ in range(len(ribbon_lengths))]

    for i in range(len(ribbon_lengths)):
        dp[i][0] = 0

    for j in range(1, total + 1):
        if j % ribbon_lengths[0] == 0:
            dp[0][j] = j // ribbon_lengths[0]

    for i in range(1, len(ribbon_lengths)):
        for j in range(1, total + 1):
            c1 = -float('infinity')
            if ribbon_lengths[i] <= j:
                c1 = dp[i][j - ribbon_lengths[i]] + 1
            c2 = dp[i - 1][j]
            dp[i][j] = max(c1, c2)

    return dp[-1][total] if dp[-1][total] != -float('infinity') else -1
