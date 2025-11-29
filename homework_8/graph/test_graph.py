import pytest
from .main import get_components

def normalize_components(components):
    return sorted([sorted(c) for c in components])

def test_get_components_empty_graph():
    graph = {}
    assert get_components(graph) == []

def test_get_components_single_node():
    graph = {1: []}
    assert get_components(graph) == [[1]]

def test_get_components_connected_component():
    graph = {
        1: [2],
        2: [1]
    }
    expected = [[1, 2]]
    assert normalize_components(get_components(graph)) == normalize_components(expected)

def test_get_components_disconnected_graph():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    expected = [[1, 2], [3, 4]]
    assert normalize_components(get_components(graph)) == normalize_components(expected)

def test_get_components_cycle():
    graph = {
        1: [2, 3],
        2: [3, 1],
        3: [1, 2]
    }
    expected = [[1, 2, 3]]
    assert normalize_components(get_components(graph)) == normalize_components(expected)

def test_get_components_complex_graph():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [5],
        5: [4]
    }
    expected = [[1, 2, 3], [4, 5]]
    assert normalize_components(get_components(graph)) == normalize_components(expected)

def test_get_components_isolated_nodes():
    graph = {
        1: [],
        2: [],
        3: []
    }
    expected = [[1], [2], [3]]
    assert normalize_components(get_components(graph)) == normalize_components(expected)
