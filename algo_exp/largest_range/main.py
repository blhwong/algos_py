def largestRange(array):
    visited = {num: False for num in array}
    left, right = array[0], array[0]
    for num in array:
        if visited[num] == False:
            visited[num] = True
            l, r = num - 1, num + 1
            while visited.get(l):
                visited[l] = True
                l -= 1
            while visited.get(r):
                visited[r] = True
                r += 1

            if r - l - 2 > right - left:
                left, right = l + 1, r - 1

    return [left, right]
