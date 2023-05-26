"""
Problem Statement
Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence, all the elements are in increasing order (from lowest to highest).

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.
Example 1:

Input: {-4,10,3,7,15}
Output: 4
Explanation: The LIS is {-4,3,7,15}.
"""


def find_lis_length(nums):
    dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]

    for curr in range(len(nums) - 1, -1, -1):
        for prev in range(curr - 1, -2, -1):
            c1 = 0
            if prev == -1 or nums[prev] < nums[curr]:
                c1 = 1 + dp[curr + 1][curr + 1]
            c2 = dp[curr + 1][prev + 1]
            dp[curr][prev + 1] = max(c1, c2)

    return dp[0][0]


def find_lis_length_recursive(nums):
    dp = [[0] * len(nums) for i in range(len(nums))]
    return recurse(nums, 0, -1, dp)


def recurse(nums, curr_idx, prev_idx, dp):
    if curr_idx >= len(nums):
        return 0
    if dp[curr_idx][prev_idx + 1] > 0:
        return dp[curr_idx][prev_idx + 1]
    c1 = 0
    if prev_idx == -1 or nums[curr_idx] > nums[prev_idx]:
        c1 = 1 + recurse(nums, curr_idx + 1, curr_idx, dp)
    c2 = recurse(nums, curr_idx + 1, prev_idx, dp)
    dp[curr_idx][prev_idx + 1] = max(c1, c2)
    return dp[curr_idx][prev_idx + 1]
