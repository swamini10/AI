from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current = queue.popleft()
        print(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def build_graph():
    graph = {}
    try:
        num_nodes = int(input("Enter the number of nodes: "))
        print("Enter the node names:")
        nodes = [input(f"Node {i+1}: ").strip() for i in range(num_nodes)]

        for node in nodes:
            graph[node] = []

        num_edges = int(input("Enter the number of edges: "))
        print("Enter each edge in the format 'source destination':")
        for _ in range(num_edges):
            edge = input().strip().split()
            if len(edge) != 2:
                print("Invalid edge format. Please enter exactly two node names separated by space.")
                continue
            src, dest = edge
            if src in graph and dest in graph:
                graph[src].append(dest)
            else:
                print(f"Invalid edge: {src} -> {dest}")
    except ValueError:
        print("Invalid input. Please enter integer values for number of nodes and edges.")
    return graph

if __name__ == "__main__":
    graph = build_graph()
    if graph:
        start_node = input("Enter the starting node: ").strip()
        if start_node in graph:
            print("\nBFS Traversal:")
            bfs(graph, start_node)
        else:
            print(f"Start node '{start_node}' not found in the graph.")
