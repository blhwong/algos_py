from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        tracker = set()

        for num in nums:
            if num in tracker:
                return num
            tracker.add(num)

    def findDuplicateCyclic(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums [i] == nums[j]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
