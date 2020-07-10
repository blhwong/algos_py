def getNthFib(n):
    prev, curr = 0, 1

    for _ in range(1, n):
        tmp = prev
        prev = curr
        curr += tmp

    return prev
