"""
Problem Statement #
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""


def search_min_diff_element(arr, key):
    left, right = 0, len(arr) - 1

    ans = arr[0]
    diff = abs(arr[0] - key)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return key
        if abs(arr[mid] - key) < diff:
            diff = abs(arr[mid] - key)
            ans = arr[mid]
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return ans
