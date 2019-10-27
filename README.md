# Amazing mazes
> Very simple maze solver, with an amazing name

## 🚧🚧 🛑 🚧🚧 WIP
Not yet completed
Currently I am unable to install pydaedalus and have stopped working on it

## What is it?
Creates maze and then solves based on specified algorithm.  This was inspired
by Michael Pound's [video on Dijkstra's algorithm](https://youtu.be/GazC3A4OQTE)
and his [video on maze solving](https://youtube.be/rop0W4QDOUI). This project
uses's Will Robert's [pydaedalus](https://github.com/wroberts/pydaedalus) to
create mazes, without it this project would probably not exist.  The only
downside is that `pydaedalus` was written for python 3.6 and is not compatible
with python 3.7.


## How does it work?
Using the pydaedalus library a maze is created according to the specified size.
Next the maze is converted to a graph, this is done so in a very ugly brought
force method.  Next the image is solved using the specified algorithm,
currently only working with Dijkstra's.  Further information into how each
algorithm is implemented is in their file.


## Example
- Create a maze
``` python
>>> from amazing import Maze
>>> m = Maze(21, 21)  # by default uses Dijkstra
```

- Solve 
``` python
>>> m.solve()
```

- Save picture of maze or save solution
``` python
>>> m.save()
>>> m.save_solution()
```
Now two files would have been created, `maze.png` and `solution.png`.

- Extras
```python
>>> print(m)
█████████████████ ███
█   █     █   █     █
█ █ █ ███ █ ███ █████
█ █   █   █         █
█ █████ ███████████ █
...
```
