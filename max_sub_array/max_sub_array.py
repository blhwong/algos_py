from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            if curr + prev > curr:
                prev += curr
            else:
                prev = curr
            if prev > ans:
                ans = prev
        return ans

    def divide_and_conquer(self, nums: List[int]) -> int:
        def max_between(low, mid, high):
            left_sum = -float('inf')
            right_sum = -float('inf')
            curr = 0
            for i in range(mid, low - 1, -1):
                curr += nums[i]
                if curr > left_sum:
                    left_sum = curr

            curr = 0

            for i in range(mid + 1, high + 1):
                curr += nums[i]
                if curr > right_sum:
                    right_sum = curr
            return left_sum + right_sum

        def solve(low, high):
            if low == high:
                return nums[low]
            mid = (low + high) // 2
            return max(solve(low, mid), solve(mid + 1, high), max_between(low, mid, high))

        return solve(0, len(nums) - 1)
