from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if not nums or nums[0] > 0 or nums[len(nums) - 1] < 0:
            return []
        zeroes = 0
        negatives = {}
        positives = {}

        for i in nums:
            if i < 0:
                if not negatives.get(i):
                    negatives[i] = 0
                negatives[i] += 1
            elif i == 0:
                zeroes += 1
            else:
                if not positives.get(i):
                    positives[i] = 0
                positives[i] += 1

        ans = set()
        if zeroes >= 3:
            ans.add((0, 0, 0))
        if zeroes >= 1:
            # find one pos and one neg
            for i in negatives.keys():
                if positives.get(abs(i)):
                    ans.add((i, 0, abs(i)))


        for i in {**negatives, **positives}:
            if i < 0:
                ## find positive
                for j in positives.keys():
                    k = -i - j
                    if k not in positives:
                        continue
                    if k == j and positives[j] - 1 < 1:
                        continue
                    ans.add(tuple(sorted((i, j, k))))
            elif i > 0:
                ## find negatives
                for j in negatives.keys():
                    k = -i - j
                    if k not in negatives:
                        continue
                    if  k == j and negatives[j] - 1 < 1:
                        continue
                    ans.add(tuple(sorted((i, j, k))))


        return [list(s) for s in ans]
