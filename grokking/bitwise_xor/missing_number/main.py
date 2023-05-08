"""
Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.
"""


def find_missing_number(arr):
    x1 = 1
    for i in range(2, len(arr) + 2):
        x1 ^= i

    x2 = arr[0]
    for i in range(1, len(arr)):
        x2 ^= arr[i]

    return x1 ^ x2
