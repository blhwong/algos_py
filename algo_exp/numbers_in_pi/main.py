def numbersInPi(pi, numbers):
    def solve(start, memo):
        if len(pi) == start:
            return -1

        if start in memo:
            return memo[start]

        ans = float('inf')
        for num in numbers:
            if pi[start:].startswith(num):
                suffix = solve(start + len(num), memo)
                ans = min(ans, suffix + 1)

        memo[start] = ans
        return ans


    ans = solve(0, {})
    return ans if ans != float('inf') else -1
