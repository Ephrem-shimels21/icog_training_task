class Graph:
    """A simple representation of a graph using an adjacency list."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_edge(self, node1, node2):
        """
        Add an edge between node1 and node2.

        Args:
            node1: The first node.
            node2: The second node.
        """
        if node1 not in self.graph:
            self.graph[node1] = [node2]
        else:
            self.graph[node1].append(node2)

        if node2 not in self.graph:
            self.graph[node2] = [node1]
        else:
            self.graph[node2].append(node1)

    def get_neighbors(self, node):
        """Return the neighbors of the given node."""
        return self.graph[node]

    def display(self):
        """Display the graph."""
        for node, edges in self.graph.items():
            print(f"{node} -> {', '.join(edges)}")
