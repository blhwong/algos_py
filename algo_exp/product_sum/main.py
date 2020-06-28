# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

def productSum(array):
    def get_sum(arr, depth):
        ans = 0
        for curr in arr:
            if type(curr) is list:
                ans += get_sum(curr, depth + 1)
            else:
                ans += curr
        return ans * depth

    return get_sum(array, 1)
