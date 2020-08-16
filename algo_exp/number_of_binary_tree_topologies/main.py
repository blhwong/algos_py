def numberOfBinaryTreeTopologies(n):
    dp = [0] * (n + 1)

    dp[0] = 1

    if n < 1:
        return dp[n]

    for i in range(1, n + 1):
        for left_nodes in range(i):
            right_nodes = i - left_nodes - 1
            dp[i] += (dp[left_nodes] * dp[right_nodes])

    return dp[n]
