def waterArea(heights):
    ans = 0
    left, right = 0, len(heights) - 1
    left_max, right_max = 0, 0
    while left < right:
        if heights[left] < heights[right]:
            left_max = max(left_max, heights[left])
            ans += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            ans += right_max - heights[right]
            right -= 1

    return ans
