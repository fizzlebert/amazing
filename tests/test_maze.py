from context import Maze, maze

import warnings

import pytest
import PIL


def test_user_warning():
    with pytest.warns(UserWarning):
        m = Maze(50, 50)


def test_create_graph():
    m = Maze(5, 5)
    m.maze = {
        0: {0: 1, 1: 0, 2: 1, 3: 1, 4: 1},
        1: {0: 1, 1: 0, 2: 1, 3: 0, 4: 1},
        2: {0: 1, 1: 0, 2: 1, 3: 0, 4: 1},
        3: {0: 1, 1: 0, 2: 0, 3: 0, 4: 1},
        4: {0: 1, 1: 0, 2: 1, 3: 1, 4: 1},
    }
    m._create_graph()
    assert m.graph == {
        (0, 1): {(1, 1): 1},
        (1, 1): {(0, 1): 1, (2, 1): 1},
        (1, 3): {(2, 3): 1},
        (2, 1): {(1, 1): 1, (3, 1): 1},
        (2, 3): {(1, 3): 1, (3, 3): 1},
        (3, 1): {(3, 2): 1, (2, 1): 1, (4, 1): 1},
        (3, 2): {(3, 1): 1, (3, 3): 1},
        (3, 3): {(3, 2): 1, (2, 3): 1},
        (4, 1): {(3, 1): 1},
    }
