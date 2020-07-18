from collections import deque

def zigzagTraverse(array):
    ans = []
    q = deque()
    q.append((0, 0))
    count = 0
    while q:
        row, col = q.popleft()
        if row + 1 < len(array):
            q.append((row + 1, col))
        elif col + 1 < len(array[0]):
            q.append((row, col + 1))

        tmp = deque()

        i, j = row, col
        while 0 <= i < len(array) and 0 <= j < len(array[0]):
            if count % 2 != 0:
                tmp.append(array[i][j])
            else:
                tmp.appendleft(array[i][j])
            i -= 1
            j += 1

        ans += list(tmp)

        count += 1


    return ans
