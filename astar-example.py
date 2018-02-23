from astar import Astar
import time
start_time = time.time()

graph = Astar()

graph.add_node("a", {"c": 6, "b": 9, "euclidean": 6})
graph.add_node("b", {"a": 9, "f": 7, "euclidean": 4})
graph.add_node("c", {"e": 6, "d": 10, "euclidean": 6})
graph.add_node("d", {"c": 10, "f": 4, "euclidean": 4})
graph.add_node("e", {"f": 9, "c": 6, "euclidean": 3})
graph.add_node("f", {"d": 6, "e": 9, "euclidean": 0})

print("Path:", (graph.shortest_path("a", "f")))
print("Finished in:", (time.time() - start_time))
