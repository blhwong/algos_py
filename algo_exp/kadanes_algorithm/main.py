def kadanesAlgorithm(array):
    if not array:
        return 0

    ans = array[0]
    curr_sum = 0
    for num in array:
        curr_sum = max(curr_sum + num, num)
        ans = max(ans, curr_sum)

    return ans
