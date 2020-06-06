"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

def max_sub_array_of_size_k(k, arr):
    start, running_sum, ans = 0, 0, 0

    for end in range(len(arr)):
        running_sum += arr[end]

        if end >= k - 1:
            ans = max(ans, running_sum)
            running_sum -= arr[start]
            start += 1

    return ans

