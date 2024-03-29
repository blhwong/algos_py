"""
Introduction #
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’. The goal is to get the maximum profit out of the items in the knapsack. Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit and the total weight does not exceed the capacity.

Problem Statement #
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
"""

def solve_knapsack_recursive(profits, weights, capacity):
    memo = [[-1] * len(weights) for _ in range(capacity + 1)]
    return recurse(profits, weights, capacity, 0, memo)


def recurse(profits, weights, curr_capacity, curr_idx, memo):
    if curr_idx >= len(weights) or curr_capacity < 0:
        return 0
    if memo[curr_capacity][curr_idx] > -1:
        return memo[curr_capacity][curr_idx]

    p1 = 0
    if weights[curr_idx] <= curr_capacity:
        new_weight = curr_capacity - weights[curr_idx]
        p1 = profits[curr_idx] + recurse(profits, weights, new_weight, curr_idx + 1, memo)
    p2 = recurse(profits, weights, curr_capacity, curr_idx + 1, memo)

    memo[curr_capacity][curr_idx] = max(p1, p2)

    return memo[curr_capacity][curr_idx]


def solve_knapsack_iterative(profits, weights, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(weights))]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, len(weights)):
        for c in range(1, capacity + 1):
            p1 = 0
            if weights[i] <= c:
                p1 = profits[i] + dp[i - 1][c - weights[i]]
            p2 = dp[i - 1][c]
            dp[i][c] = max(p1, p2)

    return dp[-1][capacity]
