from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def generate(curr, curr_sum, offset):
            if curr_sum == target:
                ans.append(curr)
                return
            if curr_sum > target:
                return

            for i in range(offset, len(candidates)):
                val = candidates[i]
                generate(curr + [val], curr_sum + val, i)


        generate([], 0, 0)
        return ans
