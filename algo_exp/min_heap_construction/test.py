from algo_exp.min_heap_construction.main import MinHeap

def test_1():
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    min_heap = MinHeap(array)
    assert min_heap.heap == [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
    min_heap.insert(76)
    assert min_heap.heap == [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
    assert min_heap.peek() == -5
    assert min_heap.remove() == -5
    assert min_heap.peek() == 2
    assert min_heap.remove() == 2
    assert min_heap.peek() == 6
    min_heap.insert(87)
    assert min_heap.heap == [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
