def subarraySort(array):
    def is_out_of_order(i, num):
        if i == 0:
            return not num <= array[i + 1]
        elif i == len(array) - 1:
            return not array[i - 1] <= num
        return not (array[i] <= array[i + 1] and array[i - 1] <= array[i])

    min_out_of_order = float('inf')
    max_out_of_order = -float('inf')
    for i in range(len(array)):
        if is_out_of_order(i, array[i]):
            min_out_of_order = min(min_out_of_order, array[i])
            max_out_of_order = max(max_out_of_order, array[i])


    if min_out_of_order == float('inf'):
        return [-1, -1]

    left, right = 0, len(array) - 1
    while array[left] <= min_out_of_order:
        left += 1

    while array[right] >= max_out_of_order:
        right -=1

    return [left, right]
