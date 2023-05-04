"""
Problem Statement #
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


def find_letter_case_string_permutations(s):
    ans = [s]

    for i in range(len(s)):
        for j in range(len(ans)):
            curr = ans[j]
            if not curr[i].isalpha():
                break
            ans.append(curr[:i] + s[i].swapcase() + curr[i+1:])

    return ans
