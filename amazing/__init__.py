"""
Amazing
=======

A simple maze solver, written in Python.  Simple usage:

    >>> from amazing import Maze
    >>> m = Maze(21, 21)
    >>> m.save()  # save a picture of the maze
    >>> m.solve()
    >>> m.save_solution()  # save picture of maze with solution

Now you should see two new files, one called maze.png, in this case it is 21
pixels by 21 pixels.  In addition a file solution.png should appear, which
will have a red line showing the solution.
"""

from .__version__ import __author__, __author_email__, __description__
from .__version__ import __license__, __title__, __version__
from .maze import Maze
