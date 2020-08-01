def quickselect(array, k):
    def partition(low, high):
        if low == high:
            return low

        pivot = array[high]
        for i in range(low, high):
            if array[i] < pivot:
                array[low], array[i] = array[i], array[low]
                low += 1

        array[low], array[high] = array[high], array[low]
        return low

    def select(low, high):
        p = partition(low, high)

        if p == k - 1:
            return array[p]

        if p > k - 1:
            return select(low, p - 1)

        return select(p + 1, high)

    return select(0, len(array) - 1)
