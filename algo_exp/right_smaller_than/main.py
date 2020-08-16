"""
              2 (0)
       -1 (0)       4 (1)
               3 (1)       11 (4)
                        5 (4)
                            8 (5)
"""

class BST:
    def __repr__(self):
        return f'{self.__dict__}'

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_child_count = 0

    def insert(self, value, ans, left_counts = 0):
        if value < self.value:
            self.left_child_count += 1
            if not self.left:
                self.left = BST(value)
                ans.append(left_counts)
            else:
                self.left.insert(value, ans, left_counts)
        else:
            curr = 1 if value > self.value else 0
            new_count = self.left_child_count + left_counts + curr
            if not self.right:
                self.right = BST(value)
                ans.append(new_count)
            else:
                self.right.insert(value, ans, new_count)


def rightSmallerThan(array):
    if not array:
        return array

    ans = [0]
    root = BST(array[-1])
    for i in reversed(range(len(array) - 1)):
        root.insert(array[i], ans)

    return list(reversed(ans))
