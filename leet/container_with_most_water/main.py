from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            l = right - left
            h = min(height[left], height[right])
            area = l * h
            if area > ans:
                ans = area
            if h == height[right]:
                right -= 1
            else:
                left += 1
        return ans
