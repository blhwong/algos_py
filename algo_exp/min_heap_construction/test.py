from unittest import TestCase, main
from algo_exp.min_heap_construction.main import MinHeap


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True

class TestSuite(TestCase):
    def test_1(self):
        array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
        min_heap = MinHeap(array)
        self.assertListEqual(min_heap.heap, [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41])
        min_heap.insert(76)
        self.assertListEqual(min_heap.heap, [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76])
        self.assertEqual(min_heap.peek(), -5)
        self.assertEqual(min_heap.remove(), -5)
        self.assertEqual(min_heap.peek(), 2)
        self.assertEqual(min_heap.remove(), 2)
        self.assertEqual(min_heap.peek(), 6)
        min_heap.insert(87)
        self.assertListEqual(min_heap.heap, [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87])

if __name__ == '__main__':
    main()
