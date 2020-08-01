"""
[61, 71, 72, 73, 0, 1, 21, 33, 45, 45]

[45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
L                M                  R

** Only apply binary search logic on the sorted side
"""

def shiftedBinarySearch(array, target):
    def search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[left] <= array[mid]: # left side sorted
            if array[mid] > target and array[left] <= target:
                # go left only if the left bound is <= target
                return search(left, mid - 1)
            return search(mid + 1, right)
        else: # right side sorted
            if array[mid] < target and array[right] >= target:
                # go right only if right bound is >= target
                return search(mid + 1, right)
            return search(left, mid - 1)

    return search(0, len(array) - 1)
