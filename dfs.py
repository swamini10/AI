#Implement depth first search algorithm and Breadth First Search algorithm, Use an
#undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree
#data structure.
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search:")
dfs(visited, graph, '5')