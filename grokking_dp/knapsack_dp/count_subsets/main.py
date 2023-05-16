"""
Problem Statement
Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number 'S'.

Example 1:

Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.
Example 2:

Input: {1, 2, 7, 1, 5}, S=9
Output: 3
The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
"""

def count_subsets(num, sum1):
    dp = [[0] * (sum1 + 1) for _ in range(len(num))]

    for i in range(len(num)):
        dp[i][0] = 1

    for j in range(1, sum1):
        dp[0][j] = 1 if num[0] == j else 0

    for i in range(1, len(num)):
        for j in range(1, sum1 + 1):
            s1 = 0
            if num[i] <= j:
                s1 = dp[i - 1][j - num[i]]
            s2 = dp[i - 1][j]
            dp[i][j] = s1 + s2

    return dp[-1][sum1]
