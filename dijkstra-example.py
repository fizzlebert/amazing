from dijkstra import Dijkstra
import time

start_time = time.time()
graph = Dijkstra()

graph.add_node("a", {"c": 6, "b": 9})
graph.add_node("b", {"a": 9, "f": 7})
graph.add_node("c", {"e": 6, "d": 10})
graph.add_node("d", {"c": 10, "f": 4})
graph.add_node("e", {"f": 9, "c": 6})
graph.add_node("f", {"d": 6, "e": 9})

print("Path: {}".format(graph.shortest_path("a", "f")))
print("Finished in: {} seconds".format(time.time() - start_time))
