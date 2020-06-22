"""
Problem Statement #
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5]
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
"""

from collections import deque

def find_order(tasks, prerequisites):
    sorted_order = []
    adjacency_list = {v: [] for v in range(tasks)}
    degree_list = {v: 0 for v in range(tasks)}

    for v,e in prerequisites:
        adjacency_list[v].append(e)
        degree_list[e] += 1

    sources = deque()
    for v, degree in degree_list.items():
        if degree == 0:
            sources.append(v)

    while sources:
        v = sources.popleft()
        sorted_order.append(v)

        children = adjacency_list[v]
        for child in children:
            degree_list[child] -= 1
            if degree_list[child] == 0:
                sources.append(child)


    return sorted_order if len(sorted_order) == tasks else []
