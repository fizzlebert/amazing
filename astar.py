"""
A simple implementation of the a* search in a graph.

Steps:
1 Update distance of neighbouring nodes in queue.
2 Remove node from queue and move to finished dictionary.
3 Move to first node in queue.
4 Repeat until at finish.
5 Start from the finish then work backwards to find optimal path.
"""
import time
start_time = time.time()


class Astar:

    graph = {}
    queue = {}
    finished = {}

    def add_node(self, node, dict):
        """Add a node to the graph in dictionary form.
        :param node name to added to graph.
        :param dict dictionary of nodes connected to specified node."""

        self.graph[node] = dict

    @staticmethod
    def min_of_dict(dict):
        """Return index of minium value of dictionary.
        :param dict dictionary with list as values."""

        for item in dict:
            if dict[item] == min(dict.values()):
                return item

    def route(self, *nodes):
        """The distance to travel a certain path.
        :param nodes tuple of nodes in route."""

        distance = 0
        for node in nodes[:-1]:
            distance += self.graph[node][nodes[nodes.index(node) + 1]]
        return distance

    def shortest_path(self, start, finish):
        """Find the shortest path from one node to another.
        :param start string of start node.
        :param finish string of finish node."""

        # initialise queue
        for item in self.graph:
            #                   distance      node  via
            self.queue[item] = [float("inf"), item, ""]

        # start has a distance of 0 and start at start
        state = start
        self.queue[start] = [0, "a", "a"]

        # keep running until at finish
        while state != finish:

            # update distance of neighbouring nodes
            for item in list(self.graph[state])[:-1]:
                distance = self.route(state, item) + self.queue[state][0] + \
                    self.graph[item][list(self.graph[item])[-1]]

                # if hasn't been visited and is less than current distance
                if item not in self.finished:
                    if self.queue[item][0] > distance:
                        self.queue[item] = [distance, item, state]

            # remove node once all neighbours have been updated
            self.finished[state] = self.queue.pop(state)

            # update state
            state = self.min_of_dict(self.queue)
        self.finished[state] = self.queue[state]

        # reverse back to find path
        path = []
        while state != start:
            path.append(self.finished[state][2])
            state = self.finished[state][2]
        path.insert(0, finish)
        path.reverse()
        return path


graph = Astar()

graph.add_node("a", {"c": 6, "b": 9, "euclidean": 6})
graph.add_node("b", {"a": 9, "f": 7, "euclidean": 4})
graph.add_node("c", {"e": 6, "d": 10, "euclidean": 6})
graph.add_node("d", {"c": 10, "f": 4, "euclidean": 4})
graph.add_node("e", {"f": 9, "c": 6, "euclidean": 3})
graph.add_node("f", {"d": 6, "e": 9, "euclidean": 0})

print("Path:", (graph.shortest_path("a", "f")))
print("Finished in:", (time.time() - start_time))
