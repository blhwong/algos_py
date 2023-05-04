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
If a set has ‘n’ distinct elements it will have n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""


def find_permutations(nums):
    ans = [[]]

    for num in nums:
        temp = []
        for subset in ans:
            for i in range(len(subset) + 1):
                temp.append(subset[:i] + [num] + subset[i:])
        ans = temp

    return ans

def find_permutations_recursive(nums):
    return permute(nums, [], [])

def permute(curr_nums, curr_result, ans):
    if len(curr_nums) == 0:
        ans.append(curr_result)
        return
    for i in range(len(curr_nums)):
        permute(curr_nums[0:i] + curr_nums[i + 1:], curr_result + [curr_nums[i]], ans)

    return ans
