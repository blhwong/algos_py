def shiftedBinarySearch(array, target):
    def search(left, right):
        if left > right:
            return -1

        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        if array[left] <= array[mid]:
            if target < array[mid] and target >= array[left]:
                return search(left, mid - 1)
            return search(mid + 1, right)
        else:
            if target > array[mid] and target <= array[right]:
                return search(mid + 1, right)
            return search(left, mid - 1)

    return search(0, len(array) - 1)
