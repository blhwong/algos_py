# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

from collections import deque

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = deque()
        q.append(self)
        while q:
            curr = q.popleft()
            array.append(curr.name)
            for child in curr.children:
                q.append(child)

        return array
