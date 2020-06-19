"""
Problem Statement #
Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
Example 4:

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.
"""


def search_next_letter(letters, key):
    low, high = 0, len(letters) - 1
    diff = float('inf')
    closest = -1

    while low <= high:
        mid = (low + high) // 2

        compare = ord(key) - ord(letters[mid])
        if 0 < compare < diff:
            diff = compare
            closest = mid

        if letters[mid] == key:
            return letters[(mid + 1) % len(letters)]
        elif letters[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return letters[(closest + 1) % len(letters)]
