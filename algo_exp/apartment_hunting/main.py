"""
        gym     school      store
b1      1       1           4
b2      0       1           3
b3      0       0           2
b4      1       1           1
b5      2       2           2
"""

def apartmentHunting(blocks, reqs):
    dp = [[float('inf')] * (len(reqs)) for _ in blocks]

    for i in range(len(blocks)):
        for j in range(len(reqs)):
            for k in range(len(blocks)):
                if blocks[k][reqs[j]]:
                    dp[i][j] = min(dp[i][j], abs(k - i))
                    if j > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])

    ans = 0

    for i in range(len(blocks)):
        if dp[i][-1] < dp[ans][-1]:
            ans = i

    return ans
