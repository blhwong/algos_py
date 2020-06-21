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
    def get_diff(s, curr_idx, dp):
        if curr_idx >= len(nums):
            return s
        if s == 0:
            return 0

        s_idx = int(s * 2)

        if dp[curr_idx][s_idx] is not None:
            return dp[curr_idx][s_idx]

        part1 = float('inf')
        if nums[curr_idx] <= s:
            part1 = get_diff(s - nums[curr_idx], curr_idx + 1, dp)

        part2 = get_diff(s, curr_idx + 1, dp)
        dp[curr_idx][s_idx] = min(part1, part2)
        return min(part1, part2)

    total_sum = sum(nums)
    dp = [[None] * (total_sum + 1) for _ in range(len(nums))]
    return get_diff(total_sum / 2, 0, dp) * 2


def get_minimum_subset_difference_iterative(nums):
    total_sum = sum(nums)
    s = int(total_sum / 2)
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


    for j in range(s, -1, -1):
        if dp[-1][j]:
            return abs(2 * j - total_sum)
