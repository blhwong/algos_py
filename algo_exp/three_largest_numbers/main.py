from collections import deque

def replace(q, i, num):
    q.insert(i + 1, num)
    q.popleft()

def findThreeLargestNumbers(array):
    ans = deque([-float('inf')] * 3)

    for num in array:
        if num > ans[2]:
            replace(ans, 2, num)
        elif num > ans[1]:
            replace(ans, 1, num)
        elif num > ans[0]:
            replace(ans, 0, num)

    return list(ans)
