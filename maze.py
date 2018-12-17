"""
Create a maze and solve it of a maze and solve it.

Steps:
1. Create maze using the daedalus library.
2. Convert maze to graph.
3. Solve maze with algorithim.
"""

from daedalus import Maze as maze
from dijkstra import Dijkstra
from astar import Astar
from PIL import Image


class Maze:

    WHITE = (0, 0, 0)
    BLACK = (255, 255, 255)
    RED = (255, 0, 0)

    def __init__(self, algorithim, width, height):
        """Set algorithim to be used when solving.
        Args:
            algorithim (str) to be used when solving maze
        """

        self.algorithim = algorithim
        if not width % 2 or not height % 2:
            print(
                "Using even number width or height use even number for optimal images"
            )
        self.create_maze(width, height)
        self.create_graph()

    def list_to_dict(self, list):
        """Convert the maze to a list with key being index of value.
        Args:
            list (list) to be converted
        Returns:
            dict of list.
        """
        dict = {}
        for index in range(len(list)):
            dict[index] = list[index]
        return dict

    def create_maze(self, width, height):
        """Make maze to be solved and add border to maze.
        Args:
            width (int) of maze
            height (int) of maze
        """

        # create maze
        self.maze = maze(width, height)
        self.maze.create_perfect()

        # define maze variables
        self.entrance = self.maze.entrance
        self.exit = self.maze.exit

        # convert to list
        self.maze = list(self.maze)

        # add index to maze
        for index in range(len(self.maze)):
            self.maze[index] = self.list_to_dict(self.maze[index])
        self.maze = self.list_to_dict(self.maze)

    def create_graph(self):
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

    def save(self):
        """Save maze locally as an image."""
        # invert maze because maze is incorrect
        data = []
        for row in self.maze:
            for item in self.maze[row].values():
                if item:
                    data.append(self.WHITE)
                else:
                    data.append(self.BLACK)
        # save maze
        image = Image.new("RGB", (len(self.maze[0]), len(self.maze)))
        image.putdata(data)
        image.save("maze.png")

    def solve(self):
        """Solve maze using specified algorithim.
        Returns:
            shortest path as a queue from start to finish of maze
        """
        # TODO: be able to change algorithim
        algorithim = Astar()
        # algorithim = Dijkstra()
        # add nodes to graph
        for node in self.graph:
            algorithim.add_node(node, self.graph[node])
        # pydaedalus stores y then x value which need to be reversed
        self.entrance = tuple(reversed(self.entrance))
        self.exit = tuple(reversed(self.exit))
        self.path = algorithim.shortest_path(self.entrance, self.exit)

    def save_solution(self):
        """Save maze image and the shortest path."""
        data = []
        print(self.path)
        for row_i, row in enumerate(list(self.maze)):
            for item_i, item in enumerate(self.maze[row].values()):
                if (row_i, item_i) in self.path:
                    data.append(self.RED)
                elif item:
                    data.append(self.WHITE)
                else:
                    data.append(self.BLACK)

        image = Image.new("RGB", (len(self.maze[0]), len(self.maze)))
        image.putdata(data)
        image.save("solution.png")

    def __str__(self):
        """Just cause it looks nice"""
        string = []
        for row in self.maze:
            string.append(["█" if item else " " for item in self.maze[row].values()])
        return "\n".join(["".join(line) for line in string])
