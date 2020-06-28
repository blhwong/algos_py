def getNthFib(n):
    i, prev, curr = 1, 0, 1

    while i < n:
        tmp = curr
        curr = prev + curr
        prev = tmp
        i += 1

    return prev
