from .exceptions import MazeNotSolved, AlgorithmNotFound
from .dijkstra import Dijkstra
from .astar import Astar

from functools import wraps
import warnings

from daedalus import Maze as _maze
from PIL import Image

warnings.simplefilter("once", UserWarning)


class Maze:
    """
    Create a maze and solve it.

    Available algorithms:
        dijkstra
        astar (WIP)

    Steps:
    1. Create maze using the daedalus library.
    2. Convert maze to graph.
    3. Solve maze with algorithm.
    """

    WHITE = (0, 0, 0)
    BLACK = (255, 255, 255)
    RED = (255, 0, 0)

    def __init__(self, width, height, algorithm="dijkstra"):
        """Set algorithm to be used when solving.
        Args:
            algorithm (str) to be used when solving maze
            width (int) of maze in pixels
            height (int) of maze in pixels
        """

        self.algorithm = algorithm
        if not width % 2 or not height % 2:
            warnings.warn(
                "Using even width or height, use even numbers for optimal images"
            )
        self._create_maze(width, height)
        self._create_graph()
        self.width = width
        self.height = height

    def _create_maze(self, width, height):
        """Make maze to be solved and add border to maze.
        Args:
            width (int) of maze
            height (int) of maze
        """

        # create maze
        self.maze = _maze(width, height)
        self.maze.create_perfect()

        # define maze variables
        self.entrance = self.maze.entrance
        self.exit = self.maze.exit

        # add index to maze
        self.maze = {
            row_i: {item_i: item for item_i, item in enumerate(row)}
            for row_i, row in enumerate(self.maze)
        }

    def _create_graph(self):
        """Remove unnecessary states from maze and convert maze to graph to be
        solved."""

        self.graph = {}

        # convert to graph
        for column in self.maze.keys():
            for row in self.maze[column].keys():
                item = self.maze[column][row]
                if item != 1:
                    neighbours = []
                    try:
                        if self.maze[column][row - 1] != 1:
                            neighbours.append(["left", (column, row - 1)])
                    except KeyError:
                        None
                    try:
                        if self.maze[column][row + 1] != 1:
                            neighbours.append(["right", (column, row + 1)])
                    except KeyError:
                        None
                    try:
                        if self.maze[column - 1][row] != 1:
                            neighbours.append(["above", (column - 1, row)])
                    except KeyError:
                        None
                    try:
                        if self.maze[column + 1][row] != 1:
                            neighbours.append(["below", (column + 1, row)])
                    except KeyError:
                        None
                    self.graph[(column, row)] = {x[:][1]: 1 for x in neighbours}
        # TODO: remove unnecessary states

    def _maze_maker(file_name):
        def real_decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                data = []
                for row_i, row in enumerate(list(self.maze)):
                    for item_i, item in enumerate(self.maze[row].values()):
                        func(self, data, item, row_i=row_i, item_i=item_i)

                # save maze
                image = Image.new("RGB", (self.width, self.height))
                image.putdata(data)
                image.save(file_name)

            return wrapper

        return real_decorator

    @_maze_maker("maze.png")
    def save(self, data, item, row_i=None, item_i=None):
        """Save maze locally as an image."""
        # invert maze because maze is incorrect
        if item:
            data.append(self.WHITE)
        else:
            data.append(self.BLACK)

    def solve(self):
        """ Solve maze using specified algorithm.
        Returns:
            shortest path as a queue from start to finish of maze
        """
        if self.algorithm == "astar":
            algorithm = Astar()
        elif self.algorithm == "dijkstra":
            algorithm = Dijkstra()
        else:
            raise AlgorithmNotFound(
                f"Invalid algorithm: {self.algorithm}.  See help({type(self).__name__}) for available algorithms."
            )
        # add nodes to graph
        for node in self.graph:
            algorithm.add_node(node, self.graph[node])
        # pydaedalus stores y then x value which need to be reversed
        self.entrance = tuple(reversed(self.entrance))
        self.exit = tuple(reversed(self.exit))
        self.path = algorithm.shortest_path(self.entrance, self.exit)

    @_maze_maker("solution.png")
    def save_solution(self, data, item, row_i=None, item_i=None):
        """Save maze image and the shortest path."""
        if not hasattr(self, "path"):
            raise MazeNotSolved(
                f"Maze must be solved to save solution. Run {type(self).__name__}.solve() first."
            )
        if (row_i, item_i) in self.path:
            data.append(self.RED)
        elif item:
            data.append(self.WHITE)
        else:
            data.append(self.BLACK)

    def __str__(self):
        """Just cause it looks nice."""
        string = []
        for row in self.maze:
            string.append(["█" if item else " " for item in self.maze[row].values()])
        return "\n".join(["".join(line) for line in string])

    def __repr__(self):
        """Easier on the eyes."""
        return f"Maze(algorithm='{self.algorithm}', width={self.width}, height={self.height})"
