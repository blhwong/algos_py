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

from collections import deque

def make_squares_deque(arr):
    d = deque()
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] ** 2 > arr[j] ** 2:
            d.appendleft(arr[i] ** 2)
            i += 1
        else:
            d.appendleft(arr[j] ** 2)
            j -= 1

    return list(d)


def make_squares(arr):
    squares = [0 for _ in arr]
    i = 0
    j = len(arr) - 1
    k = len(arr) - 1

    while i <= j:
        if arr[i] ** 2 > arr[j] ** 2:
            squares[k] = arr[i] ** 2
            i += 1
        else:
            squares[k] = arr[j] ** 2
            j -= 1
        k -= 1

    return squares


def make_squares_outward(arr):
    squares = []
    i, j = -1, -1
    k = 0

    while k < len(arr):
        if arr[k] >= 0:
            i, j = k, k - 1
            break
        k += 1

    while j >= 0 and i < len(arr):
        if arr[i] ** 2 > arr[j] ** 2:
            squares.append(arr[j] ** 2)
            j -= 1
        else:
            squares.append(arr[i] ** 2)
            i += 1

    while i < len(arr):
        squares.append(arr[i] ** 2)
        i += 1

    while j >= 0:
        squares.append(arr[j] ** 2)
        j -= 1

    return squares

