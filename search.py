from collections import deque


class Search:
    def __init__(self, graph):
        """
        Initialize the Search class with a graph.

        Args:
            graph: An instance of the Graph class representing the graph.
        """
        self.graph = graph

    def bfs(self, source, destination):
        """
        Perform a Breadth-First Search from source to destination.

        Args:
            source: The starting node.
            destination: The node to search for.

        Returns:
            A list representing the path from source to destination, or
            None if no path was found.
        """
        visited = {source}
        queue = deque([(source, [source])])

        while queue:
            (vertex, path) = queue.popleft()
            for next_node in self.graph.get_neighbors(vertex):
                if next_node not in visited:
                    if next_node == destination:
                        return path + [next_node]
                    visited.add(next_node)
                    queue.append((next_node, path + [next_node]))
        return None

    def dfs(self, source, destination):
        """
        Perform a Depth-First Search from source to destination.

        Args:
            source: The starting node.
            destination: The node to search for.

        Returns:
            A list representing the path from source to destination, or
            None if no path was found.
        """
        visited = {source}
        stack = [(source, [source])]

        while stack:
            (vertex, path) = stack.pop()
            for next_node in self.graph.get_neighbors(vertex):
                if next_node not in visited:
                    if next_node == destination:
                        return path + [next_node]
                    visited.add(next_node)
                    stack.append((next_node, path + [next_node]))
        return None
