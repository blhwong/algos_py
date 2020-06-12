"""
Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.

1 2 3 4 5 6 7 8 9
xxxxx   xxx xxxxx
  xxx   xxxxx
"""


def merge(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1
    while i < len(intervals_a) and j < len(intervals_b):
        a = intervals_a[i]
        b = intervals_b[j]

        a_start_within_b = b[start] <= a[start] <= b[end]
        b_start_within_a = a[start] <= b[start] <= a[end]

        a_and_b_overlap = a_start_within_b or b_start_within_a

        if a_and_b_overlap:
            result.append([max(a[start], b[start]), min(a[end], b[end])])

        if a[end] < b[end]:
            i += 1
        else:
            j += 1

    return result
