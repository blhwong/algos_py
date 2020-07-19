"""
     Z  X  V  V   Y   Z      W
X   ''  x  x  x   x   x      x
K   ''  x  x  x   x   x      x
Y   ''  x  x  x  xy  xy     xy
K   ''  x  x  x  xy  xy     xy
Z    z  z  z  z  xy  xyz   xyz
P    z  z  z  z  xy  xyz   xyz
W    z  z  z  z  xy  xyz  xyzw
"""

def longestCommonSubsequence(str1, str2):
    dp = [[]] * (len(str1) + 1)

    for j in range(len(str2)):
        if str2[j] not in str1:
            continue
        for i in range(1, len(dp)):
            if str1[i - 1] == str2[j] and str2[j] not in dp[i]:
                dp[i] = dp[i] + [str2[j]]
            else:
                dp[i] = dp[i] if len(dp[i]) > len(dp[i - 1]) else dp[i - 1]

    return dp[-1]
