"""
0, []
10, [10]
80, [10, 70]
30, [10, 20]
60, [10, 20, 30]
110, [10, 20, 30, 50]
21, [10, 11]
60, [10, 20, 30]
"""

def maxSumIncreasingSubsequence(array):
    dp = [[] for _ in range(len(array))]
    dp[0] = [array[0], [array[0]]]

    for i in range(1, len(array)):
        tmp = [array[i], [array[i]]]
        for j in range(i):
            s, curr = dp[j]
            if s + array[i] > tmp[0] and curr[-1] < array[i]:
                tmp = [s + array[i], curr + [array[i]]]

        dp[i] = tmp

    ans = dp[0]
    for i in range(1, len(dp)):
        s, curr = dp[i]
        if s > ans[0]:
            ans = [s, curr]

    return ans
