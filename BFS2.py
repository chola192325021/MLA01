from collections import deque

graph = {
    'A': ['2', '3'],
    'B': ['5', '6'],
    'C': ['4', '7'],
    'D': ['8'],
    'E': [],
    'F': [],
    'G': ['8','3']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


bfs(graph, 'A')
