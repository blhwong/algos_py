"""
Introduction
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.

Example:

Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5', here are those ways:
  1. {1,1,1,1,1}
  2. {1,1,1,2}
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}
Problem Statement
Given a number array to represent different coin denominations and a total amount 'T', we need to find all the different ways to make a change for 'T' with the given coin denominations. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.
"""


def count_change(denominations, total):
    dp = [[0] * (total + 1) for _ in range(len(denominations))]

    for i in range(len(denominations)):
        dp[i][0] = 1

    for j in range(1, total + 1):
        dp[0][j] = dp[0][j - denominations[0]]

    for i in range(1, len(denominations)):
        for j in range(1, total + 1):
            c1 = 0
            if denominations[i] <= j:
                c1 = dp[i][j - denominations[i]]
            c2 = dp[i - 1][j]
            dp[i][j] = c1 + c2

    return dp[-1][total]
