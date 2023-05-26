"""
Problem Statement
Given a number sequence, find the length of its Longest Alternating Subsequence (LAS). A subsequence is considered alternating if its elements are in alternating order.

A three element sequence (a1, a2, a3) will be an alternating sequence if its elements hold one of the following conditions:

{a1 > a2 < a3 } or { a1 < a2 > a3}.
Example 1:

Input: {1,2,3,4}
Output: 2
Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
Example 2:

Input: {3,2,1,4}
Output: 3
Explanation: The LAS are {3,2,4} and {2,1,4}.
Example 3:

Input: {1,3,2,4}
Output: 4
Explanation: The LAS is {1,3,2,4}.
"""


def find_las_length(nums):
    dp1 = [[-1] * len(nums) for _ in range(len(nums))]
    dp2 = [[-1] * len(nums) for _ in range(len(nums))]
    return max(recurse(nums, -1, 0, True, dp1), recurse(nums, -1, 0, False, dp2))


def recurse(nums, prev, curr, is_asc, dp):
    if curr >= len(nums):
        return 0
    if dp[prev][curr] > -1:
        return dp[prev][curr]
    c1 = 0

    if is_asc:
        if prev == -1 or nums[prev] < nums[curr]:
            c1 = 1 + recurse(nums, curr, curr + 1, not is_asc, dp)
    else:
        if prev == -1 or nums[prev] > nums[curr]:
            c1 = 1 + recurse(nums, curr, curr + 1, not is_asc, dp)

    c2 = recurse(nums, prev, curr + 1, is_asc, dp)

    dp[prev][curr] = max(c1, c2)
    return max(c1, c2)
