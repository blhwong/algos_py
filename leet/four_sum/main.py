from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        return self.k_sum(nums, target, 4)


    def k_sum(self, nums, target, k):
        ans = []
        if not nums or not (nums[0] * k <= target <= nums[-1] * k):
            return ans
        if k == 2:
            return self.two_sum(nums, target)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for _, pair in enumerate(self.k_sum(nums[i + 1:], target - nums[i], k - 1)):
                ans.append([nums[i]] + pair)

        return ans

    def two_sum(self, nums, target):
        left, right = 0, len(nums) - 1
        pairs = []

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < target or (left > 0 and nums[left] == nums[left - 1]):
                left += 1
            elif curr_sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                right -= 1
            else:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1

        return pairs

