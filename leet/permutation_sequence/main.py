import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        ans = ''
        while nums:
            f = math.factorial(len(nums) - 1)
            i = 0
            while k > f:
                i += 1
                k -= f

            ans += nums.pop(i)

        return ans
