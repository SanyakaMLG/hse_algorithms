from queue import PriorityQueue

def dijkstra(graph: dict[int, list[tuple[int, int]]], start: int) -> dict[int, int]:
    q = PriorityQueue()
    q.put((0, start))
    p = {start: None}
    
    dist = {i: float('inf') for i in graph.keys()}
    dist[start] = 0
    
    while not q.empty():
        d, u = q.get()
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                q.put((dist[v], v))
                p[v] = u
    
    return dist, p


def get_path(p: dict[int, int], start: int, end: int) -> list[int]:
    path = []
    while end != start:
        path.append(end)
        end = p[end]
    path.append(start)
    return path[::-1]


if __name__ == '__main__':
    graph = {
        1: [(2, 1), (3, 4)],
        2: [(1, 1), (3, 2), (4, 5)],
        3: [(1, 4), (2, 2), (4, 1)],
        4: [(2, 5), (3, 1)]
    }
    dist, p = dijkstra(graph, 1)
    print(dist)
    print(get_path(p, 1, 4))
