def threeNumberSum(array, targetSum):
    def two_sum(target, left, curr):
        ans = []
        right = len(array) - 1
        while left < right:
            curr_sum = array[left] + array[right]
            if curr_sum == target:
                ans.append([curr, array[left], array[right]])
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

        return ans

    array.sort()
    ans = []
    for i in range(len(array) - 1):
        curr = array[i]
        ans += two_sum(targetSum - curr, i + 1, curr)

    return ans
