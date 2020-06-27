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
    triplets = []
    def pair_with_targetsum(arr, targetsum, left, triplets):
        right = len(arr) - 1
        while left < right:
            curr = arr[left] + arr[right]
            if curr == targetsum:
                triplets.append([-targetsum, arr[left], arr[right]])
                curr_left, curr_right = arr[left], arr[right]
                while curr_left == arr[left] and left < right:
                    left += 1
                while curr_right == arr[right] and left < right:
                    right -= 1
            elif curr < targetsum:
                left += 1
            else:
                right -= 1
        return

    arr.sort()

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        pair_with_targetsum(arr, -arr[i], i + 1, triplets)


    return triplets
