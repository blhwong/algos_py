from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        tracker = set()

        for num in nums:
            if num in tracker:
                return num
            tracker.add(num)

    def findDuplicateCyclic(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                j = nums[i] - 1
                if nums [i] == nums[j]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

    def findDuplicateCycleStart(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        curr = nums[nums[slow]]
        cycle_length = 1

        while curr != nums[slow]:
            cycle_length += 1
            curr = nums[curr]

        p1, p2 = nums[0], nums[0]

        while cycle_length > 0:
            p2 = nums[p2]
            cycle_length -= 1

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1
