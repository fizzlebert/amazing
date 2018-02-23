"""Create a maze and solve it of a maze and solve it.

1 Create maze.
2 Convert maze to graph.
2 Remove unnecessary states from maze.
3 Solve maze with algorithim.
"""

from daedalus import Maze
from dijkstra import Dijkstra
from PIL import Image


class Solve:

    def __init__(self, algorithim):
        """Set algorithim to be used when solving.
        Args:
            algorithim (str) to be used when solving maze
        """

        self.algorithim = algorithim

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
        # because a border is added
        self.maze = Maze(width - 2, height - 2)
        self.maze.create_perfect()

        # define maze variables
        self.entrance = self.maze.entrance
        self.exit = self.maze.exit

        # convert to list
        self.maze = list(self.maze)

        # add boarder, entrance and exit
        self.maze.insert(0, [1] * (width - 3))
        self.maze[0].insert(self.entrance[0], 0)

        self.maze.insert(len(self.maze), [1] * (width - 3))
        self.maze[-1].insert(self.exit[1], 0)

        for item in self.maze:
            item.insert(0, 1)
            item.insert(len(item), 1)

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
                    self.graph[(column, row)] = {x[:][1]: 1 for x in
                                                 neighbours}
        # TODO: remove unnecessary states

    def save_maze(self):
        """Save maze locally as an image."""
        # invert maze because maze is incorrect
        self.data = []
        for row in self.maze:
            for item in self.maze[row].values():
                if item == 1:
                    self.data.append(0)
                else:
                    self.data.append(1)
        # save maze
        image = Image.new("1", (len(self.maze[0]), len(self.maze)))
        image.putdata(self.data)
        image.save("image.png")

    def solve_maze(self):
        """Solve maze using specified algorithim.
        Returns:
            shortest path as a queue from start to finish of maze
        """
        algorithim = Dijkstra()
        for node in self.graph:
            algorithim.add_node(node, self.graph[node])
        self.entrance = [entrance + 1 for entrance in self.entrance]
        self.exit = [exit + 1 for exit in self.exit]
        self.entrance.reverse()
        self.exit.reverse()
        self.path = algorithim.shortest_path(tuple(self.entrance),
                                             tuple(self.exit))

    def save_solution(self):
        """Save maze image and the shortest path.
        """


solver = Solve("dijkstra")
solver.create_maze(1000, 1000)
print("Created maze")
for row in solver.maze:
    print(solver.maze[row].values())
solver.create_graph()
print("Created graph")
solver.save_maze()
print("Save maze")
solver.solve_maze()
print("Solved maze")
