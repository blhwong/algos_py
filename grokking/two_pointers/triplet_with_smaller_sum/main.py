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
    for i in range(len(arr) - 2):
        num = arr[i]
        ans += find_pairs(arr, i + 1, target - num)
    return ans

def find_pairs(arr, i, target):
    ans = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < target:
            ans += j - i
            i += 1
        else:
            j -= 1

    return ans

def triplet_with_smaller_sum_results(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        num = arr[i]
        find_pairs_results(arr, i, target - num, triplets)
    return triplets

def find_pairs_results(arr, first, target, triplets):
    left = first + 1
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] < target:
            for i in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1
