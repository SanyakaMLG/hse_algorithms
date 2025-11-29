import pytest
from .main import dag, find_cycle

def test_dag_simple_dag():
    graph = {
        1: [2],
        2: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert result == [1, 2]

def test_dag_disconnected_dag():
    graph = {
        1: [],
        2: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert set(result) == {1, 2}

def test_dag_simple_cycle():
    graph = {
        1: [2],
        2: [1]
    }
    has_cycle, cycle = dag(graph)
    assert has_cycle is True
    assert len(cycle) >= 3
    assert cycle[0] == cycle[-1]

def test_dag_self_loop():
    graph = {
        1: [1]
    }
    has_cycle, cycle = dag(graph)
    assert has_cycle is True
    assert cycle == [1, 1]

def test_dag_complex_dag():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert result.index(1) < result.index(2)
    assert result.index(1) < result.index(3)
    assert result.index(2) < result.index(4)
    assert result.index(3) < result.index(4)

def test_find_cycle_no_cycle():
    graph = {
        1: [2],
        2: []
    }
    assert find_cycle(graph) == []

def test_find_cycle_with_cycle():
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    cycle = find_cycle(graph)
    assert cycle is not None
    assert len(cycle) > 0
    assert cycle[0] == cycle[-1]

def test_dag_empty():
    graph = {}
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert result == []

def test_dag_linear_chain():
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert result == [1, 2, 3, 4, 5]

def test_dag_binary_tree():
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6, 7],
        4: [],
        5: [],
        6: [],
        7: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert result.index(1) < result.index(2)
    assert result.index(1) < result.index(3)
    assert result.index(2) < result.index(4)
    assert result.index(2) < result.index(5)
    assert result.index(3) < result.index(6)
    assert result.index(3) < result.index(7)

def test_dag_diamond():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    assert result.index(1) < result.index(2)
    assert result.index(1) < result.index(3)
    assert result.index(2) < result.index(4)
    assert result.index(3) < result.index(4)

def test_dag_disconnected_mixed():
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: [3],
        5: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is True
    assert len(result) >= 3
    assert result[0] == result[-1]
    assert set(result).issubset({3, 4})

def test_dag_large_complex():
    graph = {
        1: [2, 5],
        2: [3, 4],
        3: [6],
        4: [6],
        5: [6],
        6: [7, 8],
        7: [],
        8: []
    }
    has_cycle, result = dag(graph)
    assert has_cycle is False
    
    positions = {node: i for i, node in enumerate(result)}
    
    assert positions[1] < positions[2]
    assert positions[1] < positions[5]
    assert positions[2] < positions[3]
    assert positions[2] < positions[4]
    assert positions[3] < positions[6]
    assert positions[4] < positions[6]
    assert positions[5] < positions[6]
    assert positions[6] < positions[7]
    assert positions[6] < positions[8]
