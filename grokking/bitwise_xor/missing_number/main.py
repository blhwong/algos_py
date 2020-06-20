"""
Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.
"""


def find_missing_number(arr):
    x1 = 0
    for i in range(len(arr) + 1):
        x1 ^= i + 1

    x2 = 0
    for i in range(len(arr)):
        x2 ^= arr[i]

    return x1 ^ x2
