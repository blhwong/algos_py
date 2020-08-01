def quickSort(array):
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

    def sort(low, high):
        if high < low:
            return
        p = partition(low, high)
        if low < p - 1:
            sort(low, p - 1)
        if p < high:
            sort(p + 1, high)

    sort(0, len(array) - 1)
    return array
