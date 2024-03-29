"""
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""

def smallest_subarray_with_given_sum(s, arr):
    ans = float('infinity')
    start = 0
    curr_sum = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum >= s:
            ans = min(ans, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    return ans if ans != float('infinity') else 0
