def searchForRange(array, target):
    def search(find_max):
        left, right = 0, len(array) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                ans = mid
                if find_max:
                    left = mid + 1
                else:
                    right = mid - 1
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    return [search(False), search(True)]
