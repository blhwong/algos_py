from typing import List

"""
[1, 1, 2, 6]
[24, 12, 4, 1]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = [1]
        right = [1]

        for i in range(len(nums) - 1):
            left.append(left[-1] * nums[i])

        for i in reversed(range(1, len(nums))):
            right.append(right[-1] * nums[i])

        for i in range(len(nums)):
            ans.append(left[i] * right[-1 - i])

        return ans
