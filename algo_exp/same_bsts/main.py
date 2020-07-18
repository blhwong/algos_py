def sameBsts(arrayOne, arrayTwo):
    if not arrayOne and not arrayTwo:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False

    l1, r1, l2, r2 = [], [], [], []

    root = arrayOne[0]

    for i in range(1, len(arrayOne)):
        if arrayOne[i] < root:
            l1.append(arrayOne[i])
        else:
            r1.append(arrayOne[i])

        if arrayTwo[i] < root:
            l2.append(arrayTwo[i])
        else:
            r2.append(arrayTwo[i])

    return sameBsts(l1, l2) and sameBsts(r1, r2)
