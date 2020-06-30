def longestPeak(array):
    ans = 0

    for i in range(1, len(array) - 1):
        prev = i - 1
        curr = i
        nxt = i + 1

        if array[curr] > array[prev] and array[curr] > array[nxt]:
            left, right = prev, nxt
            while left > 0 and array[left - 1] < array[left]:
                left -= 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1

            ans = max(ans, right - left + 1)

    return ans
