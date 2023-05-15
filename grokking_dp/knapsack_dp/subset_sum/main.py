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
"""

def has_sum(nums, s):
    dp = [[None] * (s + 1) for _ in range(len(nums))]

    for i in range(len(nums)):
        dp[i][0] = True

    for j in range(1, s + 1):
        dp[0][j] = nums[0] == j

    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            ans1 = False
            if nums[i] <= j:
                ans1 = dp[i - 1][j - nums[i]]
            ans2 = dp[i - 1][j]
            dp[i][j] = ans1 or ans2

    return dp[-1][s]
