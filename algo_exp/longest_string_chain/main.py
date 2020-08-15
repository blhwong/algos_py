def by_length(x):
    return len(x)

def get_chains(curr, tracker, curr_chain, memo):
    if curr not in tracker:
        return curr_chain
    if curr in memo:
        return memo[curr]

    curr_chain.append(curr)

    sub_chain = []
    for i in range(len(curr)):
        new = curr[0:i] + curr[i + 1:]
        sub_chain = max(sub_chain, get_chains(new, tracker, [], memo), key=by_length)

    memo[curr] = curr_chain + sub_chain
    return memo[curr]

def longestStringChain(strings):
    ans = []
    tracker = set(strings)
    memo = {}

    strings.sort(key=by_length, reverse=True)

    for string in strings:
        chain = get_chains(string, tracker, [], memo)
        ans = max(ans, chain, key=by_length)

    return ans if len(ans) > 1 else []
