"""
Problem Statement
Given a rod of length 'n', we are asked to cut the rod and sell the pieces in a way that will maximize the profit. We are also given the price of every piece of length 'i' where '1 <= i <= n'.

Example:

Lengths: [1, 2, 3, 4, 5]
Prices: [2, 6, 7, 10, 13]
Rod Length: 5

Let's try different combinations of cutting the rod:

Five pieces of length 1 => 10 price
Two pieces of length 2 and one piece of length 1 => 14 price
One piece of length 3 and two pieces of length 1 => 11 price
One piece of length 3 and one piece of length 2 => 13 price
One piece of length 4 and one piece of length 1 => 12 price
One piece of length 5 => 13 price

This shows that we get the maximum price (14) by cutting the rod into two pieces of length '2' and one piece of length '1'.
"""


def solve_rod_cutting(lengths, prices, n):
    dp = [[0] * (n + 1) for _ in range(len(lengths))]

    for j in range(1, n + 1):
        if lengths[0] <= j:
            dp[0][j] = prices[0] + dp[0][j - lengths[0]]

    for i in range(1, len(lengths)):
        for j in range(1, n + 1):
            p1 = 0
            if lengths[i] <= j:
                p1 = prices[i] + dp[i][j - lengths[i]]
            p2 = dp[i - 1][j]
            dp[i][j] = max(p1, p2)

    return dp[-1][n]
