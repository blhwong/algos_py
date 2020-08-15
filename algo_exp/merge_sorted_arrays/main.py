from heapq import heappush, heappop

def mergeSortedArrays(arrays):
    ans = []
    min_heap = []

    for idx, array in enumerate(arrays):
        heappush(min_heap, (array[0], idx, 0))

    while min_heap:
        val, source_idx, arr_idx = heappop(min_heap)
        source_array = arrays[source_idx]
        if arr_idx + 1 < len(source_array):
            heappush(min_heap, (source_array[arr_idx + 1], source_idx, arr_idx + 1))
        ans.append(val)

    return ans
