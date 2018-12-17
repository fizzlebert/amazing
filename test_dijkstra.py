from errors import NodeNotFound
from dijkstra import Dijkstra

import pytest

graph = Dijkstra()


def test_scenario():
    graph.add_node("a", {"c": 6, "b": 9})
    graph.add_node("b", {"a": 9, "f": 7})
    graph.add_node("c", {"e": 6, "d": 10})
    graph.add_node("d", {"c": 10, "f": 4})
    graph.add_node("e", {"f": 9, "c": 6})
    graph.add_node("f", {"d": 6, "e": 9})

    assert graph.shortest_path("a", "f") == ["a", "b", "f"]


def test_unknown_node():
    with pytest.raises(NodeNotFound):
        graph.shortest_path("a", "g")
