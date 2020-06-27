from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = []

        def pair_with_target_sum(arr, target_sum, left, triplets):
            right = len(arr) - 1
            while left < right:
                curr = arr[left] + arr[right]
                if curr == target_sum:
                    triplets.append([-target_sum, arr[left], arr[right]])
                    left_num, right_num = arr[left], arr[right]
                    while arr[left] == left_num and left < right:
                        left += 1

                    while arr[right] == right_num and left < right:
                        right -= 1

                elif curr < target_sum:
                    left += 1
                else:
                    right -= 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pair_with_target_sum(nums, -nums[i], i + 1, triplets)

        return triplets
