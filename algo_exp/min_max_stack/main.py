# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.storage = []
        self.min_max_storage = []

    def peek(self):
        return self.storage[-1]

    def pop(self):
        self.min_max_storage.pop()
        return self.storage.pop()

    def push(self, number):
        self.storage.append(number)
        curr_min = self.getMin() if self.min_max_storage else number
        curr_max = self.getMax() if self.min_max_storage else number
        self.min_max_storage.append((min(curr_min, number), max(curr_max, number)))

    def getMin(self):
        return self.min_max_storage[-1][0]

    def getMax(self):
        return self.min_max_storage[-1][1]
