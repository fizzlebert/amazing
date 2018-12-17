"""
A simple implementation of the dijkstra search in a graph.

Steps:
1. Update distance of neighbouring nodes in queue.
2. Remove node from queue and move to finished dictionary.
3. Move to first node in queue.
4. Repeat until at finish.
5. Start from the finish then work backwards to find optimal path.
"""

from collections import deque

from errors import NodeNotFound


class Dijkstra:

    graph = {}
    queue = {}
    finished = {}

    def add_node(self, node, dic):
        """Add a node to the graph in dictionary form.
        Args:
            node (str): name to added to graph.
            dic (dict) dictionary of nodes connected to specified node.
        """

        self.graph[node] = dic

    @staticmethod
    def min_of_dict(dic):
        """Return index of minium value of dictionary.
        Args:
            dict (dict) dictionary with list as values.
        Returns:
            minium value of dict.
        """

        for item in dic:
            if dic[item] == min(dic.values()):
                return item

    def route(self, *nodes):
        """The distance to travel a certain path.
        Args:
            nodes (tuple) of nodes.
        Returns:
            length of route.
        """

        distance = 0
        for node in nodes[:-1]:
            distance += self.graph[node][nodes[nodes.index(node) + 1]]
        return distance

    def shortest_path(self, start, finish):
        """Find the shortest path from one node to another.
        Args:
            start (str) of start node.
            finish (str) of finish node.
        Returns:
            shortest path in graph.
        """

        # initialise queue
        for item in self.graph:
            #                   distance      node  via
            self.queue[item] = [float("inf"), item, ""]

        # start has a distance of 0 and start at start
        state = start
        self.queue[start] = [0, "a", "a"]

        # keep running until at finish
        while state != finish:

            if state not in self.graph:
                raise NodeNotFound(state)
            # update distance of neighbouring nodes
            for item in self.graph[state]:
                distance = self.route(state, item) + self.queue[state][0]

                # if hasn't been visited and is less than current distance
                if item not in self.finished:
                    if self.queue[item][0] > distance:
                        self.queue[item] = [distance, item, state]

            # remove node once all neighbours have been updated
            self.finished[state] = self.queue.pop(state)
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
