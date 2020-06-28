def moveElementToEnd(array, toMove):
    left, right = 0, len(array) - 1
    while left < right:
        while left < right and array[right] == toMove:
            right -= 1
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array

"""
2, 1, 2, 2, 2, 3, 4, 2
4, 1, 2, 2, 2, 3, 2, 2
4, 1, 3, 2, 2, 2, 2, 2
"""
