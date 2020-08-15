def by_length(x):
    return len(x)

def get_chains(curr, tracker, curr_chain):
    if curr not in tracker:
        return curr_chain

    curr_chain.append(curr)

    sub_chain = []
    for i in range(len(curr)):
        new = curr[0:i] + curr[i + 1:]
        sub_chain = max(sub_chain, get_chains(new, tracker, []), key=by_length)

    return curr_chain + sub_chain

def longestStringChain(strings):
    ans = []
    tracker = set(strings)

    strings.sort(key=by_length, reverse=True)

    for string in strings:
        chain = get_chains(string, tracker, [])
        ans = max(ans, chain, key=by_length)

    return ans if len(ans) > 1 else []
