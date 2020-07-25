def numbersInPi(pi, numbers):
    def solve(start, memo, prefixes):
        if len(pi) == start:
            return -1

        if start in memo:
            return memo[start]

        ans = float('inf')
        for i in range(start, len(pi)):
            prefix = pi[start:i + 1]
            if prefix in prefixes:
                suffix = solve(start + len(prefix), memo, prefixes)
                ans = min(ans, suffix + 1)

        memo[start] = ans
        return ans

    ans = solve(0, {}, set(numbers))
    return ans if ans != float('inf') else -1
