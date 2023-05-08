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
from collections import deque

def find_closest_elements(arr, K, X):
    max_heap = []
    for i in range(K):
        heappush(max_heap, (-abs(arr[i] - X), arr[i]))

    for i in range(K, len(arr)):
        if abs(arr[i] - X) < -max_heap[0][0]:
            heappushpop(max_heap, (-abs(arr[i] - X), arr[i]))

    return [num for _, num in max_heap]


def find_closest_elements_bs(arr, K, X):
    max_heap = []
    closest_idx = search(arr, X)

    left, right = max(0, closest_idx - K), min(len(arr) - 1, closest_idx + K)

    for i in range(left, right + 1):
        if len(max_heap) < K:
            heappush(max_heap, (-abs(arr[i] - X), arr[i]))
        elif abs(arr[i] - X) < -max_heap[0][0]:
            heappushpop(max_heap, (-abs(arr[i] - X), arr[i]))

    return [num for _, num in max_heap]


def find_closest_elements_tp(arr, K, X):
    ans = []
    closest_idx = search(arr, X)

    if closest_idx == 0:
        return arr[:K]
    elif closest_idx == len(arr) - 1:
        return arr[-K:]

    p1, p2 = closest_idx, closest_idx + 1

    while len(ans) < K and p1 >= 0 and p2 < len(arr):
        d1 = abs(arr[p1] - X)
        d2 = abs(arr[p2] - X)

        if d1 <= d2:
            ans.append(arr[p1])
            p1 -= 1
        else:
            ans.append(arr[p2])
            p2 += 1

    while len(ans) < K and p1 >= 0:
        ans.append(arr[p1])
        p1 -= 1

    while len(ans) < K and p2 < len(arr):
        ans.append(arr[p2])
        p2 += 1

    return ans


def search(arr, key):
    left, right = 0, len(arr) - 1

    closest_idx = 0

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        if abs(arr[mid] - key) < abs(arr[closest_idx] - key):
            closest_idx = mid
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return closest_idx
