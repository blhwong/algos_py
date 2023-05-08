"""
Problem Statement #
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:

Input: [2, 1, 3, 2]
Output: [1, 3]
"""


def find_single_numbers(nums):
    n1_xor_n2 = 0
    for num in nums:
        n1_xor_n2 ^= num

    right_most_bit_set = 1
    while (right_most_bit_set & n1_xor_n2) == 0:
        right_most_bit_set <<= 1

    n1, n2 = 0, 0

    for num in nums:
        is_set = num & right_most_bit_set
        if is_set:
            n1 ^= num
        else:
            n2 ^= num

    return [n1, n2]
