from collections import deque

def findThreeLargestNumbers(array):
    ans = deque([-float('inf') for _ in range(3)])

    def replace(idx, num):
        ans.insert(idx + 1, num)
        ans.popleft()

    for num in array:
        if num > ans[2]:
            replace(2, num)
        elif num > ans[1]:
            replace(1, num)
        elif num > ans[0]:
            replace(0, num)

    return list(ans)
