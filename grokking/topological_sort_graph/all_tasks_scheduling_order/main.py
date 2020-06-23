"""
Problem Statement #
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
Example 2:

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output:
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output:
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
"""

from collections import deque

def get_order(results, curr_order, curr_source, adjacency_list, curr_degree_list):
    if not curr_source:
        results.append(curr_order)
    for v in curr_source:
        new_order = curr_order.copy()
        new_order.append(v)
        next_source = deque(curr_source)
        next_source.remove(v)
        new_degree_list = curr_degree_list.copy()

        for child in adjacency_list[v]:
            new_degree_list[child] -= 1
            if new_degree_list[child] == 0:
                next_source.append(child)

        get_order(results, new_order, next_source, adjacency_list, new_degree_list)

def get_all_orders(tasks, prerequisites):
    results = []
    adjacency_list = {v: [] for v in range(tasks)}
    degree_list = {v: 0 for v in range(tasks)}

    for v, e in prerequisites:
        adjacency_list[v].append(e)
        degree_list[e] += 1

    sources = deque()

    for v, degree in degree_list.items():
        if degree == 0:
            sources.append(v)


    get_order(results, [], sources, adjacency_list, degree_list)
    return results


def print_orders(tasks, prerequisites):
  print(get_all_orders(tasks, prerequisites))

