def twoNumberSum(array, targetSum):
    tracker = set()

    for num in array:
        diff = targetSum - num

        if diff in tracker:
            return [num, diff]
        else:
            tracker.add(num)

    return []
