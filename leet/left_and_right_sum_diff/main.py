from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = []

        ans = []

        total_sum = sum(nums)

        for i in range(len(nums) - 1):
            left_sum.append(nums[i] + left_sum[-1])
            total_sum -= nums[i]
            right_sum.append(total_sum)

        right_sum.append(0)

        for i in range(len(left_sum)):
            ans.append(abs(left_sum[i] - right_sum[i]))

        return ans
