def powerset(array):
    ans = [[]]

    for num in array:
        for i in range(len(ans)):
            ans.append(ans[i] + [num])

    return ans
