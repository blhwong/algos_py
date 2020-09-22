from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        tracker = set()

        for num in nums:
            if num in tracker:
                return num
            tracker.add(num)

