"""
    ''  Z   X   V   V   Y   Z      W
''  ''  ''  ''  ''  ''  ''  ''     ''
 X  ''  ''   x   x   x   x   x      x
 K  ''  ''   x   x   x   x   x      x
 Y  ''  ''   x   x   x  xy  xy     xy
 K  ''  ''   x   x   x  xy  xy     xy
 Z  ''   z   z   z   z  xy  xyz   xyz
 P  ''   z   z   z   z  xy  xyz   xyz
 W  ''   z   z   z   z  xy  xyz  xyzw
"""

def longestCommonSubsequence(str1, str2):
    dp = [[''] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str2[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key = lambda x: len(x))

    return list(dp[-1][-1])
