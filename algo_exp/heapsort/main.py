def compare(a, b):
    return a > b

def get_swap_idx(i, heap):
    child1_idx, child2_idx = i * 2 + 1, i * 2 + 2
    if child2_idx < len(heap) and compare(heap[child2_idx], heap[child1_idx]):
        return child2_idx
    return child1_idx

def sift_down(start, end, heap):
    curr_idx = start
    swap_idx = get_swap_idx(curr_idx, heap)
    while swap_idx < end:
        if not compare(heap[swap_idx], heap[curr_idx]):
            break
        heap[swap_idx], heap[curr_idx] = heap[curr_idx], heap[swap_idx]
        curr_idx = swap_idx
        swap_idx = get_swap_idx(curr_idx, heap)

def heapify(array):
    first_parent_idx = (len(array) - 2) // 2
    for i in reversed(range(first_parent_idx + 1)):
        sift_down(i, len(array) - 1, array)

def heapSort(array):
    heapify(array)
    for i in reversed(range(1, len(array))):
        array[0], array[i] = array[i], array[0]
        sift_down(0, i, array)
    return array
