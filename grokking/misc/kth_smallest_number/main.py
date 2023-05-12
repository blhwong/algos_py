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
    prev_smallest_idx, prev_smallest = -1, -float('infinity')
    curr_smallest_idx, curr_smallest = -1, float('infinity')
    for i in range(k):
        for j in range(len(nums)):
            if prev_smallest < nums[j] < curr_smallest:
                curr_smallest = nums[j]
                curr_smallest_idx = j
            elif nums[j] == prev_smallest and j != prev_smallest_idx:
                curr_smallest = nums[j]
                curr_smallest_idx = j

        prev_smallest = curr_smallest
        prev_smallest_idx = curr_smallest_idx
        curr_smallest = float('infinity')

    return prev_smallest

def find_Kth_smallest_number_brute_force_sorting(nums, k):
    nums.sort()
    return nums[k - 1]

def find_Kth_smallest_number_max_heap(nums, k):
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -max_heap[0]:
            heappushpop(max_heap, -nums[i])

    return -max_heap[0]

def find_Kth_smallest_number_min_heap(nums, k):
    min_heap = [num for num in nums]
    heapify(min_heap)
    for _ in range(k - 1):
        heappop(min_heap)
    return min_heap[0]

def find_Kth_smallest_number_quick_sort_partitioning(nums, k):
    def recurse(left, right):
        p = partition(left, right)

        if p == k - 1:
            return nums[p]

        if p > k - 1:
            return recurse(left, p - 1)

        return recurse(p + 1, right)

    def partition(left, right):
        if left == right:
            return left

        pivot = nums[right]
        for i in range(left, right):
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        nums[left], nums[right] = nums[right], nums[left]
        return left

    return recurse(0, len(nums) - 1)

def find_Kth_smallest_number_quick_sort_randomized_partitioning(nums, k):
    def recurse(left, right):
        p = partition(left, right)

        if p == k - 1:
            return nums[p]

        if p > k - 1:
            return recurse(left, p - 1)

        return recurse(p + 1, right)

    def partition(left, right):
        if left == right:
            return left

        pivot_idx = randint(left, right)
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        pivot = nums[right]
        for i in range(left, right):
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        nums[left], nums[right] = nums[right], nums[left]
        return left

    return recurse(0, len(nums) - 1)

def find_Kth_smallest_number_median_of_medians(nums, k):
    def recurse(left, right):
        p = partition(nums, left, right)

        if p == k - 1:
            return nums[p]

        if p > k - 1:
            return recurse(left, p - 1)

        return recurse(p + 1, right)

    def partition(partition_nums, left, right):
        if left == right:
            return left

        median = find_median(left, right)
        for i in range(left, right):
            if partition_nums[i] == median:
                partition_nums[i], partition_nums[right] = partition_nums[right], partition_nums[i]
                break

        pivot = partition_nums[right]
        for i in range(left, right):
            if partition_nums[i] < pivot:
                partition_nums[left], partition_nums[i] = partition_nums[i], partition_nums[left]
                left += 1

        partition_nums[left], partition_nums[right] = partition_nums[right], partition_nums[left]
        return left

    def find_median(left, right):
        n = right - left + 1
        if n < 5:
            return nums[left]
        partitions = [nums[i:i + 5] for i in range(left, right + 1, 5)]
        full_partitions = [partition for partition in partitions if len(partition) == 5]
        sorted_partitions = [sorted(partition) for partition in full_partitions]
        medians = [partition[2] for partition in sorted_partitions]
        return partition(medians, 0, len(medians) - 1)

    return recurse(0, len(nums) - 1)
