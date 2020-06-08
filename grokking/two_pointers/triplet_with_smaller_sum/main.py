"""
Problem Statement
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target = 3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target = 5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    ans = 0

    def pair_with_targetsum(arr, targetsum, left):
        count = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < targetsum:
                count += right - left
                left += 1
            else:
                right -= 1

        return count

    for i in range(len(arr) - 2):
        ans += pair_with_targetsum(arr, target - arr[i], i + 1)

    return ans
