"""
Minimum Deletions to Make a Sequence Sorted
Problem Statement
Given a number sequence, find the minimum number of elements that should be deleted to make the remaining sequence sorted.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 2
Explanation: We need to delete {4,1} to make the remaing sequence sorted {2,3,6,10,12}.
Example 2:

Input: {-4,10,3,7,15}
Output: 1
Explanation: We need to delete {10} to make the remaing sequence sorted {-4,3,7,15}.
Example 3:

Input: {3,2,1,0}
Output: 3
Explanation: Since the elements are in reverse order, we have to delete all except one to get a
sorted sequence. Sorted sequences are {3}, {2}, {1}, and {0}
"""


def find_minimum_deletions(nums):
    dp = [[0] * (len(nums)) for _ in range(len(nums))]

    for j in range(len(nums)):
        dp[0][j] = 1

    for i in range(1, len(nums) + 1):
        for j in range(i, len(nums)):
            c1 = 0
            if nums[j] > nums[i - 1]:
                c1 = 1 + dp[i - 1][i - 1]
            c2 = dp[i - 1][j]
            dp[i][j] = max(c1, c2)

    return len(nums) - dp[-1][-1]
