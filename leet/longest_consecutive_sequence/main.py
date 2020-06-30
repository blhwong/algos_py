from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tracker = set(nums)

        ans = 0

        for num in nums:
            if num - 1 not in tracker:
                curr_max = 1
                curr_num = num
                while (curr_num + 1) in tracker:
                    curr_num += 1
                    curr_max += 1

                ans = max(ans, curr_max)


        return ans
