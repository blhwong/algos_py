from typing import List
from collections import deque


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = { i: [] for i in range(numCourses) }
        degree_list = { i: 0 for i in range(numCourses) }

        for child, parent in prerequisites:
            adjacency_list[parent].append(child)
            degree_list[child] += 1

        q = deque()

        for v, degree in degree_list.items():
            if degree == 0:
                q.append(v)

        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for child in adjacency_list[curr]:
                degree_list[child] -= 1
                if degree_list[child] == 0:
                    q.append(child)

        return ans if len(ans) == numCourses else []
