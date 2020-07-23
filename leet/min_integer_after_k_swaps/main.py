class Solution:
    def minInteger(self, num: str, k: int) -> str:
        arr = list(num)

        swaps_left = k

        for i in range(len(arr)):
            if not swaps_left:
                break
            min_idx = i
            for j in range(i + 1, min(len(arr), i + swaps_left + 1)):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            if i != min_idx:
                swaps_left -= min_idx - i
                for j in range(min_idx, i, -1):
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]


        return ''.join(arr)
