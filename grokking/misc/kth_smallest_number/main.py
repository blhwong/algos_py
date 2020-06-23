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

from heapq import *
from random import randint


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
    return sorted(nums)[k - 1]

def find_Kth_smallest_number_max_heap(nums, k):
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        curr = nums[i]
        if curr < -max_heap[0]:
            heappushpop(max_heap, -curr)

    return -max_heap[0]

def find_Kth_smallest_number_min_heap(nums, k):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)

    ans = -1

    for _ in range(k):
        ans = heappop(min_heap)

    return ans

def find_Kth_smallest_number_quick_sort_partitioning(nums, k):
    def partition(low, high):
        if low == high:
            return low

        pivot = nums[high]
        for i in range(low, high):
            if nums[i] < pivot:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1

        nums[low], nums[high] = nums[high], nums[low]
        return low

    def quicksort(low, high):
        p = partition(low, high)

        if p == k - 1:
            return nums[p]

        if p > k - 1:
            return quicksort(low, p - 1)

        return quicksort(p + 1, high)

    return quicksort(0, len(nums) - 1)



def find_Kth_smallest_number_quick_sort_randomized_partitioning(nums, k):
    def partition(low, high):
        if low == high:
            return low

        p_idx = randint(low, high)
        nums[p_idx], nums[high] = nums[high], nums[p_idx]

        pivot = nums[high]

        for i in range(low, high):
            if nums[i] < pivot:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1

        nums[high], nums[low] = nums[low], nums[high]
        return low

    def quicksort(low, high):
        p = partition(low, high)

        if p == k - 1:
            return nums[p]

        if p > k - 1:
            return quicksort(low, p - 1)

        return quicksort(p + 1, high)

    return quicksort(0, len(nums) - 1)

def find_Kth_smallest_number_median_of_medians(nums, k):
    return -1
