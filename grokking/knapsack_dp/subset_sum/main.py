"""
Problem Statement #
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

Example 1: #
Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
Example 2: #
Input: {1, 2, 7, 1, 5}, S=10
Output: True
The given set has a subset whose sum is '10': {1, 2, 7}
Example 3: #
Input: {1, 3, 4, 8}, S=6
Output: False
The given set does not have any subset whose sum is equal to '6'.

    0  1  2  3  4  5  6
1 0 F  T  F  F  F  F  F
2 1
3 2
7 3
"""

def has_sum(nums, s):
    dp = [[False] * (s + 1) for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for j in range(s + 1):
        dp[0][j] = nums[0] == j

    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif nums[i] <= j:
                dp[i][j] = dp[i - 1][j - nums[i]]

    return dp[-1][s]
