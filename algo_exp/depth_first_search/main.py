# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        def traverse(curr):
            if not curr:
                return

            array.append(curr.name)

            for child in curr.children:
                traverse(child)

        traverse(self)
        return array
