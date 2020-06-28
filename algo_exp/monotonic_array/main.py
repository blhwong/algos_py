def isMonotonic(array):
    is_increasing = None
    for i in range(len(array) - 1):
        j = i + 1
        num_i = array[i]
        num_j = array[j]
        if is_increasing is None:
            if num_i < num_j:
                is_increasing = True
            elif num_i > num_j:
                is_increasing = False
        else:
            if num_i < num_j and not is_increasing:
                return False
            elif num_i > num_j and is_increasing:
                return False

    return True
