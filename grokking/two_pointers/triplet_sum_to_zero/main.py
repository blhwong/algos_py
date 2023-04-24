"""
Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""


def search_triplets(arr):
    arr.sort()
    ans = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        num = arr[i]
        find_pairs(arr, i + 1, -num, ans)

    return ans

def find_pairs(arr, i, target, triplets):
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            triplets.append([-target, arr[i], arr[j]])
            i += 1
            j -= 1
            while i < j and arr[i] == arr[i - 1]:
                i += 1
            while i < j and arr[j] == arr[j + 1]:
                j -= 1
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
