def smallestDifference(arrayOne, arrayTwo):
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        closest = float('inf')
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            compare = abs(arr[mid] - target)
            if 0 < compare < closest:
                closest = compare
                ans = arr[mid]

            if arr[mid] == target:
                return target
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    arrayOne.sort()
    ans = None
    closest = float('inf')
    for num2 in arrayTwo:
        num1 = binary_search(arrayOne, num2)
        compare = abs(num1 - num2)
        if compare < closest:
            closest = compare
            ans = [num1, num2]

    return ans
