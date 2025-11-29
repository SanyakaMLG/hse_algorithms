def dfs(graph: dict[int, list[int]], start: int, visited: set[int] | None = None) -> list[int]:
    if visited is None:
        visited = set()

    visited.add(start)
    component = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            component.extend(dfs(graph, neighbor, visited))
    
    return component


def get_components(graph: dict[int, list[int]]) -> list[list[int]]:
    components = []
    visited = set()
    for i in graph.keys():
        if i not in visited:
            components.append(dfs(graph, i, visited))
    return components


if __name__ == '__main__':
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [5],
        5: [4]
    }
    
    components = get_components(graph)
    print(components)
