"""
Problem Statement #
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]
"""


def find_range(arr, key):
    left = find(arr, key, True)
    right = find(arr, key, False)

    return [left, right]


def find(arr, key, is_find_min_index):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            ans = mid
            if is_find_min_index:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return ans
