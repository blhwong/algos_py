"""
Problem Statement #
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Example 1:

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.
Example 2:

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.
Example 3:

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.
Example 4:

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.
"""


def search_ceiling_of_a_number(arr, key):
    def search(low, high, m, closest):
        if high < low:
            return closest

        mid = high - low // 2

        if 0 < arr[mid] - key < m:
            m = arr[mid] - key
            closest = mid

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            return search(mid + 1, high, m, closest)

        return search(low, mid - 1, m, closest)

    return search(0, len(arr) - 1, float('inf'), -1)

def search_floor_of_a_number(arr, key):
    def search(low, high, m, closest):
        if high < low:
            return closest

        mid = high - low // 2

        if 0 < key - arr[mid] < m:
            m = key - arr[mid]
            closest = mid

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            return search(mid + 1, high, m, closest)

        return search(low, mid - 1, m, closest)

    return search(0, len(arr) - 1, float('inf'), -1)
