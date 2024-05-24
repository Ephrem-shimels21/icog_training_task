from search import Search
import csv
from graph import Graph


def read_cities(path):
    """
    Read a TXT file and return a Graph object.

    Args:
        path: The path to the TXT file.

    Returns:
        A Graph object representing the data in the TXT file.
    """
    graph = Graph()
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            graph.add_edge(row[0], row[1])
    return graph


def main():
    # Create a graph from the file
    graph = read_cities("./cities.txt")
    search = Search(graph)
    # Define the source and destination
    source = "New York"
    destination = "Miami"

    # Perform BFS and print the result
    bfs_path = search.bfs(source, destination)
    print(f"BFS path from {source} to {destination}: {bfs_path}")

    # Perform DFS and print the result
    dfs_path = search.dfs(source, destination)
    print(f"DFS path from {source} to {destination}: {dfs_path}")


if __name__ == "__main__":
    main()
