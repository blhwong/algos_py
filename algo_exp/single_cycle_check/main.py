def hasSingleCycle(array):
    fast, slow = 0, 0

    while fast < len(array):
        slow += array[slow]
        fast += array[fast]
        if fast < len(array):
            fast += array[fast]
        if slow == fast:
            return True

    return False
