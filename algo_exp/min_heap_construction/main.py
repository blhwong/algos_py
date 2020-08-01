# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    @staticmethod
    def get_parent_idx(i):
        return (i - 1) // 2

    @staticmethod
    def get_child_indices(i):
        return i * 2 + 1, i * 2 + 2

    @staticmethod
    def compare(a, b):
        return a < b

    def buildHeap(self, array):
        first_parent_idx = (len(array) - 2) // 2 # get the last parent node
        for i in reversed(range(first_parent_idx + 1)):
            # call siftdown on every parent node
            self.siftDown(i, array)

        return array

    def get_swap_idx(self, i, heap):
        # swap curr_idx with the smaller child
        child1_idx, child2_idx = self.get_child_indices(i)
        if child2_idx < len(heap) and self.compare(heap[child2_idx], heap[child1_idx]):
            return child2_idx
        return child1_idx

    def siftDown(self, start, heap):
        curr_idx = start
        swap_idx = self.get_swap_idx(curr_idx, heap)
        while swap_idx < len(heap):
            if not self.compare(heap[swap_idx], heap[curr_idx]):
                break
            heap[swap_idx], heap[curr_idx] = heap[curr_idx], heap[swap_idx]
            curr_idx = swap_idx
            swap_idx = self.get_swap_idx(curr_idx, heap)

    def siftUp(self, end, heap):
        curr_idx = end
        parent_idx = self.get_parent_idx(curr_idx)
        while curr_idx > 0 and self.compare(heap[curr_idx], heap[parent_idx]):
            heap[curr_idx], heap[parent_idx] = heap[parent_idx], heap[curr_idx]
            curr_idx = parent_idx
            parent_idx = self.get_parent_idx(curr_idx)

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        self.siftDown(0, self.heap)
        return value

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
