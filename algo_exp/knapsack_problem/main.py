"""
v w     0  1  2  3  4  5  6  7  8  9  10
1,2     0  0  1  1  1  1  1  1  1  1   1
4,3     0  0  1  4  4  5  5  5  5  5   5
5,6     0  0  1  4  4  5  5  5  6  9   9
6,7     0  0  1  4  4  5  5  6  6  9  10
"""

def knapsackProblem(items, capacity):
    dp = [[[0, []]] * (capacity + 1) for _ in range(len(items))]

    for j in range(capacity + 1):
        if items[0][1] <= j:
            dp[0][j] = [items[0][0], [0]]


    for i in range(1, len(items)):
        for j in range(1, capacity + 1):
            one = dp[i - 1][j]
            two = [0, []]
            value, weight = items[i]
            if weight <= j:
                prev_value, prev_list = dp[i - 1][j - weight]
                two = [value + prev_value, prev_list + [i]]

            dp[i][j] = max([one, two], key = lambda x: x[0])

    return dp[-1][-1]
