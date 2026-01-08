def dfs(graph, start):
    visited = set()
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

dfs(graph,'1')
