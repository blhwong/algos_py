"""
Problem Statement #
Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""

from heapq import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    @staticmethod
    def compare(l1, l2):
        if len(l1) != len(l2):
            return False

        list1 = sorted(l1, key=lambda x: x.x)
        list2 = sorted(l2, key=lambda x: x.x)

        for i in range(len(list1)):
            curr1 = list1[i]
            curr2 = list2[i]
            if curr1.x != curr2.x or curr1.y != curr2.y:
                return False

        return True


def find_closest_points(points, k):
    pass
