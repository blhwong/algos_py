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
    return k_sum(array, targetSum, 4)


def k_sum(array, target, k):
    ans = []
    if not array or not (array[0] * k <= target <= array[-1] * k):
        return ans
    if k == 2:
        return two_sum(array, target)
    for i in range(len(array)):
        for _, pairs in enumerate(k_sum(array[i + 1:], target - array[i], k - 1)):
            ans.append([array[i]] + pairs)

    return ans


def two_sum(array, target):
    pairs = []
    left, right = 0, len(array) - 1
    while left < right:
        curr_sum = array[left] + array[right]
        if curr_sum < target or (left > 0 and array[left] == array[left - 1]):
            left += 1
        elif curr_sum > target or (right < len(array) - 1 and array[right] == array[right + 1]) :
            right -= 1
        else:
            pairs.append([array[left], array[right]])
            left += 1
            right -= 1

    return pairs
