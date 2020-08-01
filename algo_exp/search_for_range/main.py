def searchForRange(array, target):
    def search(left, right, ans, find_max):
        if left > right:
            return

        mid = (left + right) // 2

        if array[mid] == target:
            if find_max:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    ans[1] = mid
                else:
                    search(mid + 1, right, ans, find_max)
            else:
                if mid == 0 or array[mid - 1] != target:
                    ans[0] = mid
                else:
                    search(left, mid - 1, ans, find_max)

        elif array[mid] < target:
            search(mid + 1, right, ans, find_max)
        else:
            search(left, mid - 1, ans, find_max)

    ans = [-1, -1]
    search(0, len(array) - 1, ans, False)
    search(0, len(array) - 1, ans, True)

    return ans
