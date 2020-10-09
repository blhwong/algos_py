"""
[61, 71, 72, 73, 0, 1, 21, 33, 45, 45]

[45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
L                M                  R

** Only apply binary search logic on the sorted side
"""

def shifted_binary_search(array, target):
    left, right = 0, len(array) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[left] <= array[mid]:
            if array[left] <= target <= array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if array[mid] <= target <= array[right]:
                left = mid + 1
            else:
                right = mid - 1

    return ans
