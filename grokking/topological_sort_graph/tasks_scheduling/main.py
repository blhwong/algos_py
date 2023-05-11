"""
Problem Statement #
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible sceduling of tasks is: [0 1 4 3 2 5]
"""

from collections import deque

def is_scheduling_possible(tasks, prerequisites):
    graph = { v: [] for v in range(tasks) }
    degree_list = { v: 0 for v in range(tasks) }

    for u, v in prerequisites:
        graph[u].append(v)
        degree_list[v] += 1

    q = deque()

    for v, degree in degree_list.items():
        if degree == 0:
            q.append(v)

    count = 0

    while q:
        v = q.popleft()
        count += 1
        children = graph[v]
        for child in children:
            degree_list[child] -= 1
            if degree_list[child] == 0:
                q.append(child)

    return count == tasks
