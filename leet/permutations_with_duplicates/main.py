from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        nums.sort()
        for curr in nums:
            tmp = []
            for subset in ans:
                for i in range(len(subset) + 1):
                    tmp.append(subset[:i] + [curr] + subset[i:])
                    if i < len(subset) and subset[i] == curr:
                        break

                ans = tmp

        return ans
