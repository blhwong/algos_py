from typing import List


class Solution:

    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in reversed(range(len(A))):
            for j in reversed(range(len(B))):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1

        return max(max(row) for row in dp)
