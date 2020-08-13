"""
    n   o   o   n   a   b   b   a   d
    0   1   2   3   4   5   6   7   8
0   T   F   F   T   F   F   F   F   F
1       T   T   F   F   F   F   F   F
2           T   F   F   F   F   F   F
3               T   F   F   F   F   F
4                   T   F   F   T   F
5                       T   T   F   F
6                           T   F   F
7                               T   F
8                                   T

0   0   1   2   0   1   2   3   4   5
1       1   1   0   1   2   3   4   5
2           1   0   1   2   3   4   5
3               0   1   2   3   4   5
4                   1   2   3   1   2
5                       2   2   1   2
6                           2   1   2
7                               1   2
8                                   2
"""

def palindromePartitioningMinCuts(string):
    palindromes = [[False] * len(string) for _ in string]

    for i in range(len(string)):
        palindromes[i][i] = True

    for j in range(1, len(string)):
        for i in range(j):
            length = j - i + 1
            if length == 2:
                palindromes[i][j] = string[i] == string[j]
            else:
                palindromes[i][j] = string[i] == string[j] and palindromes[i + 1][j - 1]

    dp = [float('inf')] * len(string)
    for j in range(len(string)):
        if palindromes[0][j]:
            dp[j] = 0
        else:
            dp[j] = dp[j - 1] + 1
            for i in range(1, j):
                if palindromes[i][j] and dp[i - 1] + 1 < dp[j]:
                    dp[j] = dp[i - 1] + 1


    return dp[-1]
