from collections import deque

def topologicalSort(jobs, deps):
    adjacency_list = {job: [] for job in jobs}
    degree_list = {job: 0 for job in jobs}

    for v, e in deps:
        adjacency_list[v].append(e)
        degree_list[e] += 1

    source = deque()

    for v, degree in degree_list.items():
        if degree == 0:
            source.append(v)

    ans = []
    while source:
        curr = source.popleft()
        ans.append(curr)
        children = adjacency_list[curr]
        for child in children:
            degree_list[child] -= 1
            if degree_list[child] == 0:
                source.append(child)

    return ans if len(ans) == len(jobs) else []
