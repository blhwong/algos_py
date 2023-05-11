"""
Problem Statement #
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
    3
    2
    0
    1
Example 2:

Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1
    4
    2
    3
    0
    1
Example 3:

Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.
"""

from collections import deque

def topological_sort(vertices, edges):
    ans = []
    adjacency_list = { v: [] for v in range(vertices) }
    degree_list = { v: 0 for v in range(vertices) }
    for u, v in edges:
        adjacency_list[u].append(v)
        degree_list[v] += 1

    q = deque()
    for v, degree in degree_list.items():
        if degree == 0:
            q.append(v)

    while q:
        v = q.popleft()
        ans.append(v)
        children = adjacency_list[v]
        for child in children:
            degree_list[child] -= 1
            if degree_list[child] == 0:
                q.append(child)

    return ans
