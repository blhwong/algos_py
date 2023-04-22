# k = 5, arr=[1, 3, 2, 6, -1, 4, 1, 8, 2])
# Result: [2.2, 2.8, 2.4, 3.6, 2.8]

def average_subarray_size_k(k, arr):
    ans = []
    curr_sum = 0
    start = 0

    for end in range(len(arr)):
        curr_sum += arr[end]

        if end + 1 >= k:
            ans.append(curr_sum / k)

            curr_sum -= arr[start]
            start += 1


    return ans
