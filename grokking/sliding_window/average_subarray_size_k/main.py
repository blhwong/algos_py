def average_subarray_size_k(k, arr):
    results = []
    running_sum = 0
    start = 0
    for end in range(len(arr)):
        running_sum += arr[end]
        if end >= k - 1:
            avg = running_sum / k
            results.append(avg)
            running_sum -= arr[start]
            start += 1
    return results
