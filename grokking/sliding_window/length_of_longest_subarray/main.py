"""
Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""


def length_of_longest_subarray(arr, k):
    ans = 0
    curr_max = 0
    start = 0
    for end in range(len(arr)):
        if arr[end] > 0:
            curr_max += 1

        if end - start + 1 - curr_max > k:
            if arr[start] > 0:
                curr_max -= 1
            start += 1

        ans = max(ans, end - start + 1)

    return ans
