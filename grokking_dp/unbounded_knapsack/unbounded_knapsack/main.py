"""
Introduction
Given the weights and profits of 'N' items, we are asked to put these items in a knapsack that has a capacity 'C'. The goal is to get the maximum profit from the items in the knapsack. The only difference between the "0/1 Knapsack" problem and this problem is that we are allowed to use an unlimited quantity of an item.

Let's take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Melon }
Weights: { 1, 2, 3 }
Profits: { 15, 20, 50 }
Knapsack capacity: 5

Let's try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.

5 Apples (total weight 5) => 75 profit
1 Apple + 2 Oranges (total weight 5) => 55 profit
2 Apples + 1 Melon (total weight 5) => 80 profit
1 Orange + 1 Melon (total weight 5) => 70 profit

This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

Problem Statement
Given two integer arrays to represent weights and profits of 'N' items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number 'C'. We can assume an infinite supply of item quantities; therefore, each item can be selected multiple times.
"""


def solve_knapsack_recursive(profits, weights, capacity):
    dp = [[-1] * (capacity + 1) for _ in range(len(profits))]
    return recurse(profits, weights, capacity, 0, dp)


def recurse(profits, weights, curr_capacity, i, dp):
    if i >= len(profits):
        return 0
    if curr_capacity < 0:
        return 0
    if dp[i][curr_capacity] > -1:
        return dp[i][curr_capacity]
    p1 = 0
    if weights[i] <= curr_capacity:
        p1 = profits[i] + recurse(profits, weights, curr_capacity - weights[i], i, dp)
    p2 = recurse(profits, weights, curr_capacity, i + 1, dp)
    dp[i][curr_capacity] = max(p1, p2)
    return dp[i][curr_capacity]


def solve_knapsack_iterative(profits, weights, capacity):
    dp = [[0] * (capacity + 1) for _ in range(len(profits))]

    for i in range(len(profits)):
        dp[i][0] = 0

    for j in range(capacity + 1):
        if weights[0] <= j:
            dp[0][j] = profits[0] + dp[0][j - weights[0]]

    for i in range(1, len(profits)):
        for j in range(1, capacity + 1):
            p1 = 0
            if weights[i] <= j:
                p1 = profits[i] + dp[i][j - weights[i]]
            p2 = dp[i - 1][j]
            dp[i][j] = max(p1, p2)

    return dp[-1][capacity]
