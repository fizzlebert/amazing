import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amazing.dijkstra import Dijkstra
from amazing.astar import Astar
from amazing.maze import Maze
from amazing import exceptions, maze
