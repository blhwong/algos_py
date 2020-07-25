def numbersInPi(pi, numbers):
    def solve(pi_left, used):
        if len(pi_left) == 0:
            return used - 1

        ans = float('inf')
        for num in numbers:
            if pi_left.startswith(num):
                ans = min(ans, solve(pi_left[len(num):], used + 1))

        return ans


    ans = solve(pi, 0)
    return ans if ans != float('inf') else -1
