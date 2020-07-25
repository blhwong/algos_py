from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i + 1 == nums[i]:
                i += 1
            elif nums[i] <= 0:
                i += 1
            elif nums[i] > len(nums):
                i += 1
            elif nums[i] == nums[nums[i]-1]:
                i += 1
            else:
                a, b = i, nums[i] - 1
                nums[a], nums[b] = nums[b], nums[a]

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1

        return len(nums) + 1
