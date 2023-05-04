"""
Problem Statement #
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

[]
[] [1]
[] [1] [1] [1, 5]
[] [1] [3] [1, 3] [3] [1, 3] [3, 3] [1, 3, 3]
"""


def find_subsets(nums):
    nums.sort()
    ans = [[]]
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = len(ans) // 2
        for j in range(start, len(ans)):
            ans.append(ans[j] + [nums[i]])

    return ans
