def getNthFib(n):
    i, prev, curr = 1, 0, 1

    while i < n:
        tmp = prev
        prev = curr
        curr += tmp
        i += 1

    return prev
