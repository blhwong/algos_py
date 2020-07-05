"""
Problem Statement #
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""

def find_permutations(nums):
    result = [[]]
    for curr in nums:
        tmp = []
        for subset in result:
            for i in range(len(subset) + 1):
                tmp.append(subset[:i] + [curr] + subset[i:])

            result = tmp


    return result

def find_permutations_recursive(nums):
    result = []
    def permute(curr, nums_left):
        if len(curr) == len(nums):
            result.append(curr)
            return

        for idx, val in enumerate(nums_left):
            permute(curr + [val], nums_left[0:idx] + nums_left[idx + 1:])

    permute([], nums)
    return result
