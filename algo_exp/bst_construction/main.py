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
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BST(value)

        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BST(value)

        return self

    def contains(self, value):
        if self.value == value:
            return True

        if self.value < value and self.right:
            return self.right.contains(value)

        if self.value > value and self.left:
            return self.left.contains(value)

        return False


    def remove(self, value, parent = None):
        if self.value < value and self.right:
            self.right.remove(value, self)
        elif self.value > value and self.left:
            self.left.remove(value, self)
        elif self.value == value:
            if self.left and self.right:
                self.value = self.right.get_min()
                self.right.remove(self.value, self)
            elif not parent:
                if self.left:
                    self.value = self.left.value
                    self.left = self.left.left
                    self.right = self.left.right
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.left if self.left else self.right
        return self

    def get_min(self):
        if not self.left:
            return self.value

        return self.left.get_min()
