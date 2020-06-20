"""
Problem Statement #
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
"""

from heapq import *

def find_closest_elements(arr, K, X):
    def search(low, high):
        diff = float('inf')
        closest = -1
        while low <= high:
            mid = (low + high) // 2

            compare = abs(arr[mid] - X)
            if 0 < compare < diff:
                diff = compare
                closest = mid


            if arr[mid] == X:
                return mid
            elif arr[mid] < X:
                low = mid + 1
            else:
                high = mid - 1

        return closest

    max_heap = []

    idx = search(0, len(arr) - 1)

    start = max(K, idx - K)
    end = min(len(arr), idx + K)

    for i in range(K):
        curr = arr[i]
        diff = abs(curr - X)
        heappush(max_heap, (-diff, curr))


    for i in range(start, end):
        curr = arr[i]
        diff = abs(curr - X)

        if diff < -max_heap[0][0]:
            heappushpop(max_heap, (-diff, curr))


    return [ans for diff, ans in max_heap]
