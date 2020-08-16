def merge(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr2[j] < arr1[i]:
            merged.append(arr2[j])
            j += 1
        else:
            merged.append(arr1[i])
            i += 1

    return merged + arr1[i:] + arr2[j:]


def mergeSort(array):
    size = len(array)
    if size == 1:
        return array

    half = size // 2

    return merge(mergeSort(array[0:half]), mergeSort(array[half:]))
