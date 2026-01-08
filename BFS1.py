from collections import deque

graph = {
    '1': ['2', '7'],
    '2': ['1', '3', '6'],
    '3': ['2', '4','5'],
    '4': [],
    '5': [],
    '6': [],
    '7': ['1','8','10'],
    '8': ['7','9'],
    '9': [],
    '10':[]
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
