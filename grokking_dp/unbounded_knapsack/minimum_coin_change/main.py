"""
Introduction
Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.

Example 1:

Denominations: {1,2,3}
Total amount: 5
Output: 2
Explanation: We need a minimum of two coins {2,3} to make a total of '5'
Example 2:

Denominations: {1,2,3}
Total amount: 11
Output: 4
Explanation: We need a minimum of four coins {2,3,3,3} to make a total of '11'
Problem Statement
Given a number array to represent different coin denominations and a total amount 'T', we need to find the minimum number of coins needed to make a change for 'T'. We can assume an infinite supply of coins, therefore, each coin can be chosen multiple times.
"""


def count_change(denominations, total):
    dp = [[0] * (total + 1) for _ in range(len(denominations))]

    for j in range(1, total + 1):
        dp[0][j] = denominations[0] + dp[0][j - denominations[0]]

    for i in range(1, len(denominations)):
        for j in range(1, total + 1):
            c1 = float('infinity')
            if denominations[i] <= j:
                c1 = dp[i][j - denominations[i]] + 1
            c2 = dp[i - 1][j]
            dp[i][j] = min(c1, c2)

    return dp[-1][total]
