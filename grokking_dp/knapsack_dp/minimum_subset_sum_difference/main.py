"""
Problem Statement #
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2: #
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3: #
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""

def get_minimum_subset_difference_recursive(nums):
    s = sum(nums)
    dp = [[None] * (s + 1) for _ in range(len(nums))]
    return recurse(nums, 0, 0, 0, dp)

def recurse(nums, i, p1, p2, dp):
    if i >= len(nums):
        return abs(p1 - p2)
    if dp[i][p1] is not None:
        return dp[i][p1]
    if dp[i][p2] is not None:
        return dp[i][p2]

    ans1 = recurse(nums, i + 1, p1 + nums[i], p2, dp)
    ans2 = recurse(nums, i + 1, p1, p2 + nums[i], dp)
    dp[i][p1] = min(ans1, ans2)
    return dp[i][p1]

def get_minimum_subset_difference_iterative(nums):
    s = sum(nums) // 2

    dp = [[0] * (s + 1) for _ in range(len(nums))]

    for j in range(1, s + 1):
        dp[0][j] = nums[0]

    for i in range(1, len(nums)):
        for j in range(1, s + 1):
            c1 = 0
            if nums[i] <= j:
                c1 = nums[i] + dp[i - 1][j - nums[i]]
            c2 = dp[i - 1][j]
            dp[i][j] = max(c1, c2)

    return abs(dp[-1][s] - sum(nums) / 2) * 2
