from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in reversed(range(last_pos)):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0
