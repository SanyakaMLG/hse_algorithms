import pytest
from .main import dijkstra, get_path

def test_dijkstra_simple_path():
    graph = {
        1: [(2, 10)],
        2: []
    }
    dist, p = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 10
    assert p[2] == 1
    assert get_path(p, 1, 2) == [1, 2]

def test_dijkstra_unreachable():
    graph = {
        1: [(2, 10)],
        2: [],
        3: []
    }
    dist, p = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 10
    assert dist[3] == float('inf')
    
    with pytest.raises(KeyError):
        get_path(p, 1, 3)

def test_dijkstra_better_path():
    graph = {
        1: [(2, 10), (3, 2)],
        2: [],
        3: [(2, 3)]
    }
    dist, p = dijkstra(graph, 1)
    assert dist[2] == 5
    assert p[2] == 3
    assert get_path(p, 1, 2) == [1, 3, 2]

def test_dijkstra_cycle_positive_weights():
    graph = {
        1: [(2, 1)],
        2: [(1, 1)]
    }
    dist, p = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 1

def test_dijkstra_start_equals_end():
    graph = {
        1: [(2, 1)],
        2: []
    }
    dist, p = dijkstra(graph, 1)
    assert dist[1] == 0
    assert get_path(p, 1, 1) == [1]

def test_dijkstra_complex_graph():
    graph = {
        1: [(2, 1), (3, 4)],
        2: [(1, 1), (3, 2), (4, 5)],
        3: [(1, 4), (2, 2), (4, 1)],
        4: [(2, 5), (3, 1)]
    }
    dist, p = dijkstra(graph, 1)
    assert dist[4] == 4
    assert get_path(p, 1, 4) == [1, 2, 3, 4]
