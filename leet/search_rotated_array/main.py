from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(left, right):
            if right < left:
                return -1
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            left_side = left, mid - 1
            right_side = mid + 1, right

            if nums[mid] < target:
                if target < nums[right]:
                    # go right
                    res = bin_search(*right_side)
                    if res != -1:
                        return res
                    return bin_search(*left_side)
                else:
                    res = bin_search(*left_side)
                    if res != -1:
                        return res
                    return bin_search(*right_side)
            if nums[mid] > target:
                if nums[left] < target:
                    # go left
                    res = bin_search(*left_side)
                    if res != -1:
                        return res
                    return bin_search(*right_side)
                else:
                    res = bin_search(*right_side)
                    if res != -1:
                        return res
                    return bin_search(*left_side)

        return bin_search(0, len(nums) - 1)
