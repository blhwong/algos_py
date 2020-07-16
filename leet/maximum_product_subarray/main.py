from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans, min_so_far, max_so_far = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            prev_min, prev_max = min_so_far, max_so_far
            min_so_far = min(num, prev_min * num, prev_max * num)
            max_so_far = max(num, prev_min * num, prev_max * num)
            ans = max(ans, max_so_far)

        return ans
