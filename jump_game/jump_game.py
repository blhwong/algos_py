from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in reversed(range(last_pos)):
            if i + nums[i] >= last_pos:
                last_pos = i

        return last_pos == 0

    def bottom_up(self, nums: List[int]) -> bool:
        dp = [None for _ in range(len(nums))]
        dp[len(nums) - 1] = True

        for i in reversed(range(len(nums) - 1)):
            furthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0] == True
