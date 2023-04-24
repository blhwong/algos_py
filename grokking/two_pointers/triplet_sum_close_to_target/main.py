"""
Problem Statement
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target = 2
Output: 1
Explanation: The triplet[-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target = 1
Output: 0
Explanation: The triplet[-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target = 100
Output: 3
Explanation: The triplet[1, 1, 1] has the closest sum to the target.
"""


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    ans = float('infinity')
    for i in range(len(arr) - 2):
        triplet = [arr[i]] + find_closest_pair(arr, i + 1, target_sum - arr[i])
        if abs(target_sum - sum(triplet)) < abs(target_sum - ans):
            ans = sum(triplet)
    return ans

def find_closest_pair(arr, i, target_sum):
    pair = []
    j = len(arr) - 1
    while i < j:
        pair = [arr[i], arr[j]]
        if arr[i] + arr[j] == target_sum:
            return [arr[i], arr[j]]
        elif arr[i] + arr[j] < target_sum:
            i += 1
        else:
            j -= 1
    return pair
