"""
Problem Statement
Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). A subsequence is considered bitonic if it is monotonically increasing and then monotonically decreasing.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LBS is {2,3,6,10,1}.
Example 2:

Input: {4,2,5,9,7,6,10,3,1}
Output: 7
Explanation: The LBS is {4,5,9,7,6,3,1}.
"""


def find_lbs_length(nums):
    ans = 0
    dp = [[0] * len(nums) for _ in range(len(nums))]
    dp_rev = [[0] * len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        c1 = recurse(nums, -1, i, dp)
        c2 = recurse_rev(nums, -1, i, dp_rev)
        ans = max(ans, c1 + c2 - 1)
    return ans


def recurse(nums, prev, curr, dp):
    if curr >= len(nums):
        return 0

    if dp[prev][curr] > 0:
        return dp[prev][curr]

    c1 = 0
    if prev < 0 or nums[prev] > nums[curr]:
        c1 = 1 + recurse(nums, curr, curr + 1, dp)

    c2 = recurse(nums, prev, curr + 1, dp)

    dp[prev][curr] = max(c1, c2)
    return dp[prev][curr]


def recurse_rev(nums, prev, curr, dp):
    if curr < 0:
        return 0

    if dp[prev][curr] > 0:
        return dp[prev][curr]

    c1 = 0
    if prev < 0 or nums[prev] > nums[curr]:
        c1 = 1 + recurse_rev(nums, curr, curr - 1, dp)
    c2 = recurse_rev(nums, prev, curr - 1, dp)

    dp[prev][curr] = max(c1, c2)
    return dp[prev][curr]
