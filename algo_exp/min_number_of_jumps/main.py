def minNumberOfJumps(array):
    dp = [float('inf')] * len(array)
    dp[0] = 0

    for i in range(1, len(array)):
        for j in range(i):
            if array[j] + j >= i:  # can it jump from current index to i
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

def minNumberOfJumpsOptimal(array):
    if len(array) == 1:
        return 0

    jumps = 0
    max_reach = array[0]
    steps = array[0]

    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, i + array[i]) # farthest jump including current index
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = max_reach - i

    return jumps + 1

