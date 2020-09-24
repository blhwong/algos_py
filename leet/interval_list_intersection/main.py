from typing import List


class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0


        while i < len(A) and j < len(B):
            a_overlaps_b = A[i][0] <= B[j][0] <= A[i][1]
            b_overlaps_a = B[j][0] <= A[i][0] <= B[j][1]

            if a_overlaps_b or b_overlaps_a:
                ans.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
