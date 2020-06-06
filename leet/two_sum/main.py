from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in tracker:
                return [tracker[compliment], idx]
            else:
                tracker[num] = idx
        return []
