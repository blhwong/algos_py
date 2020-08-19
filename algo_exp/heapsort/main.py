"""
You could heapify the array and pop heap into a new array.

In order to save space, create a max heap
Swap the largest number max_heap[0] to the end
Sift down to reorder the max_heap only up until end
"""

def compare(a, b):
    return a > b

def get_swap_idx(i, end, heap):
    child1_idx, child2_idx = i * 2 + 1, i * 2 + 2
    if child2_idx < end and compare(heap[child2_idx], heap[child1_idx]):
        return child2_idx
    return child1_idx

def sift_down(start, end, heap):
    curr_idx = start
    swap_idx = get_swap_idx(curr_idx, end, heap)
    while swap_idx < end and compare(heap[swap_idx], heap[curr_idx]):
        heap[curr_idx], heap[swap_idx] = heap[swap_idx], heap[curr_idx]
        curr_idx = swap_idx
        swap_idx = get_swap_idx(curr_idx, end, heap)

def heapify(array):
    first_parent_idx = (len(array) - 2) // 2
    for i in reversed(range(first_parent_idx + 1)):
        sift_down(i, len(array), array)

def heapSort(array):
    heapify(array)
    for end in reversed(range(1, len(array))):
        array[0], array[end] = array[end], array[0]
        sift_down(0, end, array)
    return array
