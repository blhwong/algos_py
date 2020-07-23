class Solution:
    def minInteger(self, num: str, k: int) -> str:
        if k <= 0:
            return num
        n = len(num)
        if k >= n * (n - 1) // 2:
            return ''.join(sorted(list(num)))

        for i in range(10):
            idx = num.find(str(i))
            if 0 <= idx <= k:
                return str(num[idx]) + self.minInteger(num[0:idx] + num[idx + 1:], k - idx)
