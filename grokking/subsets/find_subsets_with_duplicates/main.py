"""
Problem Statement #
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
"""


def find_subsets(nums):
    nums.sort()
    subsets = []
    subsets.append([])
    end = 0
    for i in range(len(nums)):
        start = 0
        curr = nums[i]
        prev = nums[i - 1] if i > 0 else None
        if curr == prev:
            start = end
        end = len(subsets)
        for i in range(start, end):
            subsets.append(subsets[i] + [curr])


    return subsets
