# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        curr = self
        while curr:
            if value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = BST(value)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = BST(value)
                    break

        return self

    def contains(self, value):
        curr = self
        while curr:
            if value == curr.value:
                return True
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        return False


    def remove(self, value, parent = None):
        curr = self
        while curr:
            if value < curr.value:
                parent = curr
                curr = curr.left
            elif value > curr.value:
                parent = curr
                curr = curr.right
            else:
                if curr.left and curr.right:
                    curr.value = curr.right.get_min()
                    curr.right.remove(curr.value, curr)
                elif not parent:
                    if curr.left:
                        curr.value = curr.left.value
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right:
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else:
                        pass
                elif parent.left == curr:
                    parent.left = curr.left if curr.left else curr.right
                elif parent.right == curr:
                    parent.right = curr.left if curr.left else curr.right
                break

        return self

    def get_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.value
