from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'I'],
    'D': ['I'],
    'E': [],
    'F': [],
    'G': [],
    'I': []
}
def bfs(graph, start_node):
    visited = set()
    queue = deque()
    visited.add(start_node)
    queue.append(start_node)
    while queue:
        current_node = queue.popleft()
        print(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
print("Following is the Breath-First Search:")
bfs(graph, 'A')
