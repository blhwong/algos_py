def diskStacking(disks):
    ans = []
    max_height = 0
    disks.sort(key = lambda x: x[0])
    for i in range(len(disks)):
        tmp = [disks[i]]
        height = disks[i][2]
        for j in range(i + 1, len(disks)):
            w, d, h = tmp[-1]
            curr = disks[j]
            if curr[0] > w and curr[1] > d and curr[2] > h:
                tmp.append(curr)
                height += curr[2]

        if height > max_height:
            ans = tmp
            max_height = height

    return ans
