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
    left, right = 0, len(letters) - 1
    closest_letter = letters[0]
    closest_letter_index = left

    while left <= right:
        mid = (left + right) // 2
        if letters[mid] == key:
            return letters[(mid + 1) % len(letters)]
        if closest_letter < letters[mid] < key:
            closest_letter = letters[mid]
            closest_letter_index = mid
        if letters[mid] < key:
            left = mid + 1
        else:
            right = mid - 1


    return letters[(closest_letter_index + 1) % len(letters)]
