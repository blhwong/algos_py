"""
Problem Statement
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
"""


def make_squares(arr):
    squares = [0 for _ in arr]
    left = 0
    right = len(arr) - 1
    highest = len(arr) - 1

    while left < right:
        l = arr[left] ** 2
        r = arr[right] ** 2

        if l > r:
            squares[highest] = l
            left += 1
        else:
            squares[highest] = r
            right -=1

        highest -= 1

    return squares
