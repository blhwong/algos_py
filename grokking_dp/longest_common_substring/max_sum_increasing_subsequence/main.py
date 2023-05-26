"""
Problem Statement
Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

Example 1:

Input: {4,1,2,6,10,1,12}
Output: 32
Explanation: The increaseing sequence is {4,6,10,12}.
Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
Example 2:

Input: {-4,10,3,7,15}
Output: 25
Explanation: The increaseing sequences are {10, 15} and {3,7,15}.
"""


def find_msis_iterative(nums):
    dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]

    for curr in range(len(nums) - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            c1 = 0
            if prev == - 1 or nums[curr] > nums[prev]:
                c1 = nums[curr] + dp[curr + 1][curr + 1]
            c2 = dp[curr + 1][prev + 1]
            dp[curr][prev + 1] = max(c1, c2)

    return dp[0][0]


def find_msis_recursive(nums):
    dp = [[0] * len(nums) for _ in range(len(nums))]
    return recurse(nums, -1, 0, dp)


def recurse(nums, prev_idx, curr_idx, dp):
    if curr_idx >= len(nums):
        return 0
    if dp[curr_idx][prev_idx + 1] > 0:
        return dp[curr_idx][prev_idx + 1]
    c1 = 0
    if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
        c1 = nums[curr_idx] + recurse(nums, curr_idx, curr_idx + 1, dp)

    c2 = recurse(nums, prev_idx, curr_idx + 1, dp)
    dp[curr_idx][prev_idx + 1] = max(c1, c2)
    return dp[curr_idx][prev_idx + 1]
