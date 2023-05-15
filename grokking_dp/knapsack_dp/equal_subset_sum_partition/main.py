"""
Problem Statement #
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2:

Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3:

Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.
"""


def can_partition_recursive(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False
    dp = [[None] * ((s // 2) + 1) for _ in range(len(nums))]
    return recurse(nums, 0, s // 2, dp)

def recurse(nums, i, curr_sum, dp):
    if curr_sum == 0:
        return True
    if i >= len(nums):
        return False

    if dp[i][curr_sum] is not None:
        return dp[i][curr_sum]

    ans1 = False
    if nums[i] <= curr_sum:
        ans1 = recurse(nums, i + 1, curr_sum - nums[i], dp)

    ans2 = recurse(nums, i + 1, curr_sum, dp)
    dp[i][curr_sum] = ans1 or ans2
    return dp[i][curr_sum]

def can_partition_iterative(nums):
    if sum(nums) % 2 != 0:
        return False

    s = sum(nums) // 2
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
