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


def get_order(ans, curr_results, curr_sources, graph, curr_degree_list):
    if len(curr_sources) == 0:
        ans.append(curr_results)
    for v in curr_sources:
        new_results = curr_results + [v]
        new_sources = curr_sources.copy()
        new_degree_list = curr_degree_list.copy()
        new_sources.remove(v)

        for child in graph[v]:
            new_degree_list[child] -= 1
            if new_degree_list[child] == 0:
                new_sources.add(child)

        get_order(ans, new_results, new_sources, graph, new_degree_list)


def get_all_orders(tasks, prerequisites):
    graph = { v: [] for v in range(tasks) }
    degree_list = { v: 0 for v in range(tasks) }

    for u, v in prerequisites:
        graph[u].append(v)
        degree_list[v] += 1

    ans = []
    sources = set()

    for v, degree in degree_list.items():
        if degree == 0:
            sources.add(v)
    get_order(ans, [], sources, graph, degree_list)
    return ans
