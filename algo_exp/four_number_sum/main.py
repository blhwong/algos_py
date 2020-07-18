def fourNumberSum(array, targetSum):
    all_pair_sums = {}
    ans = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            curr_sum = array[i] + array[j]
            diff = targetSum - curr_sum
            if diff in all_pair_sums:
                for pair in all_pair_sums[diff]:
                    ans.append(pair + [array[i], array[j]])

        for k in range(i):
            curr_sum = array[i] + array[k]
            if curr_sum not in all_pair_sums:
                all_pair_sums[curr_sum] = []
            all_pair_sums[curr_sum].append([array[k], array[i]])

    return ans

def fourSum(array, targetSum):
    array.sort()
    ans = []
    for i in range(len(array)):
        num = array[i]
        threeSum(array, targetSum - num, num, i + 1, ans)
    return ans


def threeSum(array, target, num1, start, ans):
    for i in range(start, len(array)):
        num2 = array[i]
        twoSum(array, target - num2, num1, num2, i + 1, ans)

def twoSum(array, target, num1, num2, left, ans):
    right = len(array) - 1
    while left < right:
        curr_sum = array[left] + array[right]
        if curr_sum == target:
            ans.append([num1, num2, array[left], array[right]])
            left += 1
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
