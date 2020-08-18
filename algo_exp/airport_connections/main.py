def get_rank(airport, graph, startingAirport, visited):
    visited.add(airport)
    count = 0
    for a in graph[airport]:
        if a != startingAirport and a not in visited:
            visited.add(a)
            count += (1 + get_rank(a, graph, startingAirport, visited))

    return count

def get_ranked_list(airports, graph, startingAirport):
    ranks = {}
    for airport in airports:
        ranks[airport] = get_rank(airport, graph, startingAirport, set())

    return sorted(list(ranks.items()), key=lambda x: x[1], reverse=True)

def dfs(airport, graph, startingAirport, visited, final_count):
    if len(visited) == final_count:
        return True
    if airport in visited:
        return False
    visited.add(airport)
    for a in graph[airport]:
        if a != startingAirport:
            done = dfs(a, graph, startingAirport, visited, final_count)
            if done:
                return True

    return False

def get_graph(airports, routes):
    graph = { airport: [] for airport in airports }
    for route in routes:
        v, e = route
        graph[v].append(e)
    return graph


def airportConnections(airports, routes, startingAirport):
    graph = get_graph(airports, routes)
    ranked_list = get_ranked_list(airports, graph, startingAirport)

    ans = 0
    visited = set()

    for airport, _ in ranked_list:
        if airport in visited:
            continue
        if airport != startingAirport:
            ans += 1
        done = dfs(airport, graph, startingAirport, visited, len(airports))
        if done:
            break

    return ans
