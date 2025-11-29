def find_cycle(graph: dict[int, list[int]]) -> list[int]:
    colors = {i: 0 for i in graph.keys()}
    path = []

    def dfs(u: int) -> list[int] | None:
        colors[u] = 1
        path.append(u)

        for v in graph[u]:
            if colors[v] == 1:
                cycle_start_index = path.index(v)
                return path[cycle_start_index:] + [v]
            if colors[v] == 0:
                cycle = dfs(v)
                if cycle:
                    return cycle

        colors[u] = 2
        path.pop()
        return None

    for u in graph.keys():
        if colors[u] == 0:
            cycle = dfs(u)
            if cycle:
                return cycle
    return []

def dag(graph: dict[int, list[int]]) -> tuple[bool, list[int]]:
    if cycle := find_cycle(graph):
        return (True, cycle)
    
    res = []
    in_count = {i: 0 for i in graph.keys()}
    for i in graph.values():
        for j in i:
            in_count[j] += 1
    
    queue = [i for i in in_count if in_count[i] == 0]
    
    while queue:
        u = queue.pop(0)
        res.append(u)
        for v in graph[u]:
            in_count[v] -= 1
            if in_count[v] == 0:
                queue.append(v)
    
    return (False, res)


if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [3],
        3: [1],
        4: [5],
        5: [4]
    }
    print(dag(graph))
