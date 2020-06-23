"""
Problem Statement #
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three smaller numbers are
[1, 2, 5].
Example 3:

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""


def find_Kth_smallest_number_brute_force(nums, k):
    prev_idx = -1
    min_idx = -1
    prev_val = -float('inf')
    min_val = float('inf')
    for j in range(k):
        for i, num in enumerate(nums):
            if prev_val < num < min_val:
                min_val = num
                min_idx = i
            elif num == prev_val and i > prev_idx:
                min_val = num
                min_idx = i
                break

        prev_val = min_val
        prev_idx = min_idx
        min_val = float('inf')
        min_idx = -1


    return prev_val

def find_Kth_smallest_number_brute_force_sorting(nums, k):
    return -1

def find_Kth_smallest_number_max_heap(nums, k):
    return -1

def find_Kth_smallest_number_min_heap(nums, k):
    return -1

def find_Kth_smallest_number_quick_sort_partitioning(nums, k):
    return -1

def find_Kth_smallest_number_quick_sort_randomized_partitioning(nums, k):
    return -1

def find_Kth_smallest_number_median_of_medians(nums, k):
    return -1
