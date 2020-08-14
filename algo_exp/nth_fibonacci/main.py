# 0  1  1  2  3  5  8  13
# n begins at 1

def getNthFib(n):
    prev, curr = 0, 1

    for _ in range(1, n):
        tmp = prev
        prev = curr
        curr += tmp

    return prev
