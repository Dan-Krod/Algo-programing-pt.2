import csv
from collections import deque
from typing import Dict, List

def bfs(graph: Dict[str, Dict[str, int]], start: str, end: str, parent: Dict[str, str]) -> bool:
    """
    Perform Breadth-First Search to find a path from start to end in the residual graph.
    Args:
        graph (Dict[str, Dict[str, int]]): The residual graph represented as a dictionary of dictionaries.
        start (str): The start node.
        end (str): The end node.
        parent (Dict[str, str]): A dictionary to store the parent of each node in the path.
    Returns:
        bool: True if a path from start to end is found, False otherwise.
    """
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor, capacity in graph[node].items():
            if capacity > 0 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == end:
                    return True

    return False


def build_graph(farms: List[str], lines: List[List[str]], stores: List[str]) -> Dict[str, Dict[str, int]]:
    """
    Build the graph from the farms, lines, and stores data.
    Args:
        farms (List[str]): List of farms.
        lines (List[List[str]]): List of lines representing connections between cities and their capacities.
        stores (List[str]): List of stores.
    Returns:
        Dict[str, Dict[str, int]]: The constructed graph.
    """
    graph = {}
    for farm in farms:
        lines.append(["F", farm, float("inf")])
    for store in stores:
        lines.append([store, "S", float("inf")])
    for line in lines:
        start_city, end_city, weight = line
        if start_city not in graph:
            graph[start_city] = {}
        if end_city not in graph:
            graph[end_city] = {}
        graph[start_city][end_city] = weight
        graph[end_city][start_city] = weight
    return graph


def get_min_flow_in_path(graph: Dict[str, Dict[str, int]], path: List[str]) -> int:
    """
    Calculate the minimum flow in a given path.
    Args:
        graph (Dict[str, Dict[str, int]]): The residual graph.
        path (List[str]): The path from source to sink.
    Returns:
        int: The minimum flow in the path.
    """
    min_weight = float("inf")
    for vertex_idx in range(len(path) - 1):
        weight = get_neighbor_edge_weight(graph, path, vertex_idx)
        if weight < min_weight:
            min_weight = weight
    return min_weight


def remove_min_flow_from_vertices_in_path(graph: Dict[str, Dict[str, int]], path: List[str], min_flow: int, vertex_idx: int) -> None:
    """
    Update the residual capacities of edges in the given path after augmenting flow.
    Args:
        graph (Dict[str, Dict[str, int]]): The residual graph.
        path (List[str]): The path from source to sink.
        min_flow (int): The minimum flow in the path.
        vertex_idx (int): Index of the vertex in the path.
    """
    start_city = path[vertex_idx]
    end_city = path[vertex_idx + 1]
    graph[start_city][end_city] -= min_flow


def get_neighbor_edge_weight(graph: Dict[str, Dict[str, int]], path: List[str], vertex_idx: int) -> int:
    """
    Get the weight of the edge between two consecutive vertices in the path.
    Args:
        graph (Dict[str, Dict[str, int]]): The residual graph.
        path (List[str]): The path from source to sink.
        vertex_idx (int): Index of the current vertex in the path.
    Returns:
        int: The weight of the edge.
    """
    start_city = path[vertex_idx]
    end_city = path[vertex_idx + 1]
    return graph[start_city][end_city]


def get_path(previous: Dict[str, str], start_vertex: str, last_vertex: str) -> List[str]:
    """
    Reconstructs the path from the start vertex to the last vertex using the previous dictionary.
    Args:
        previous (Dict[str, str]): A dictionary that maps each vertex to its previous vertex in the shortest path.
        start_vertex (str): The starting vertex.
        last_vertex (str): The last vertex.
    Returns:
        List[str]: The reconstructed path from the start vertex to the last vertex.
    """
    path = []
    while last_vertex != start_vertex:
        path.append(last_vertex)
        last_vertex = previous[last_vertex]
    path.append(start_vertex)
    path.reverse()
    return path

def find_max_flow(farms: List[str], lines: List[List[str]], stores: List[str], start: str, end: str) -> int:
    """
    Find the maximum flow from farms to stores using Ford-Fulkerson algorithm.
    Args:
        farms (List[str]): List of farms.
        lines (List[List[str]]): List of lines representing connections between cities and their capacities.
        stores (List[str]): List of stores.
        source (str): The source node.
        sink (str): The sink node.
    Returns:
        int: The maximum flow from farms to stores.
    """
    graph = build_graph(farms, lines, stores)
    max_flow_value = 0
    while True:
        parent = {}
        if not bfs(graph, start, end, parent):
            break
        path = get_path(parent, start, end)
        minimum = get_min_flow_in_path(graph, path)
        max_flow_value += minimum
        for vertex_idx in range(len(path) - 1):
            remove_min_flow_from_vertices_in_path(graph, path, minimum, vertex_idx)

    return max_flow_value


def read_data_and_find_max_flow(input_file: str) -> int:
    """
    Read data from CSV file and find the maximum flow.
    Args:
        input_file (str): The path to the input CSV file.
    Returns:
        int: The maximum flow from farms to stores.
    """
    with open(f'resources/{input_file}')as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]
        if len(data) < 2:
            return -1

        farms = data[0]
        stores = data[1]
        lines = [[row[0], row[1], int(row[2])] for row in data[2:]]

    max_flow = find_max_flow(farms, lines, stores, "F", "S")
    return max_flow